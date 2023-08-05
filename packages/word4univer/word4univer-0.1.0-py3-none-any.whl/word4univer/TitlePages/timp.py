from .. import Path
from ..Word import Document
from ..Word.rels import RelType, Xml


def timp(document: Document) -> None:
    first_footer = Xml(RelType.FOOTER, "footer_first.xml", Path.get_docparts("footers/first.xml"))
    default_footer = Xml(RelType.FOOTER, "footer_default.xml", Path.get_docparts("footers/default.xml"))

    context = {
        'first_footer_id': document.add_relation(first_footer),
        'default_footer_id': document.add_relation(default_footer)
    }
    document.add_step('title_pages/timp', **context)
