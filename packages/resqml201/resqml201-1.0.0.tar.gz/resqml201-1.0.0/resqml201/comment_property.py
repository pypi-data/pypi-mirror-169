from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_comment_property import ObjCommentProperty

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class CommentProperty(ObjCommentProperty):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
