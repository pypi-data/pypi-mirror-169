from .. import Path
from ..Word import Document
from ..Word.rels import Image, RelType, Xml


def tstu(document: Document) -> None:
    logo_rel = Image(Path.get_src("images/tstu.wmf"), "tstu")
    first_footer = Xml(RelType.FOOTER, "footer_first.xml", Path.get_docparts("footers/first.xml"))
    default_footer = Xml(RelType.FOOTER, "footer_default.xml", Path.get_docparts("footers/default.xml"))

    context = {
        'logo_id': document.add_relation(logo_rel),
        'first_footer_id': document.add_relation(first_footer),
        'default_footer_id': document.add_relation(default_footer)
    }
    document.add_step('title_pages/tstu', **context)
