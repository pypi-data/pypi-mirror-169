# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2018-2021 Andrew Rechnitzer
# Copyright (C) 2020-2022 Colin B. Macdonald
# Copyright (C) 2020 Victoria Schuster

from PyQt5.QtCore import QLineF, QPointF
from PyQt5.QtGui import QPen, QColor, QBrush
from PyQt5.QtWidgets import QGraphicsLineItem, QGraphicsItem

from plom.client.tools import CommandMoveItem, CommandTool, DeleteObject


class CommandLine(CommandTool):
    def __init__(self, scene, pti, ptf):
        super().__init__(scene)
        self.scene = scene
        # A line from pti(nitial) to ptf(inal)
        self.obj = LineItem(pti, ptf, scene.style)
        self.do = DeleteObject(self.obj.shape())
        self.setText("Line")

    @classmethod
    def from_pickle(cls, X, *, scene):
        """Reconstruct from a serialized form."""
        assert cls.__name__.endswith(X[0]), 'Type "{}" mismatch: "{}"'.format(X[0], cls)
        X = X[1:]
        if len(X) != 4:
            raise ValueError("wrong length of pickle data")
        return cls(scene, QPointF(X[0], X[1]), QPointF(X[2], X[3]))


class LineItem(QGraphicsLineItem):
    def __init__(self, pti, ptf, style):
        super().__init__()
        self.saveable = True
        self.pti = pti
        self.ptf = ptf
        self.setLine(QLineF(self.pti, self.ptf))
        self.restyle(style)

        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges)

    def restyle(self, style):
        self.normal_thick = style["pen_width"]
        self.setPen(QPen(style["annot_color"], style["pen_width"]))

    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemPositionChange and self.scene():
            # If the position changes then do so with an redo/undo command
            command = CommandMoveItem(self, value)
            self.scene().undoStack.push(command)
        return super().itemChange(change, value)

    def pickle(self):
        return [
            self.__class__.__name__.replace("Item", ""),  # i.e., "Line",
            self.pti.x() + self.x(),
            self.pti.y() + self.y(),
            self.ptf.x() + self.x(),
            self.ptf.y() + self.y(),
        ]

    def paint(self, painter, option, widget):
        if not self.scene().itemWithinBounds(self):
            # paint a bounding rectangle out-of-bounds warning
            painter.setPen(QPen(QColor(255, 165, 0), 8))
            painter.setBrush(QBrush(QColor(255, 165, 0, 128)))
            painter.drawRoundedRect(option.rect, 10, 10)
        super().paint(painter, option, widget)
