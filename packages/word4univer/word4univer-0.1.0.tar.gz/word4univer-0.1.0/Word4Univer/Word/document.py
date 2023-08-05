import datetime
from io import BytesIO
from os import PathLike
from zipfile import ZipFile

import jinja2

from .rels import Relation, RelType, Xml
from .. import Path


class Document:
    EMPTY_DOC_FOLDER = "/empty_doc/"
    STYLES_FOLDER = "/styles/"
    SHARED_TEMPLATES = [
        Path.get_src("/docparts/"),
        Path.get_src(EMPTY_DOC_FOLDER)
    ]

    def __init__(self,
                 container: str | PathLike[str] | BytesIO,
                 style: str | PathLike[str] = None,
                 parts_folder: str | PathLike[str] = None,
                 **params):
        """
        Class for creating doc files
        :param container: container for saving doc file (path, or BytesIO)
        :param style: path to doc style file
        :param parts_folder: folder with xml template files
        :param params: Additional params
        :keyword jinja_globals: dict with jinja global objects
        """
        def create_jinja_env() -> jinja2.Environment:
            global_vars = {
                'date': datetime.date.today(),
                **params.get('jinja_globals', {})
            }

            folders = self.SHARED_TEMPLATES
            if parts_folder:
                folders.append(parts_folder)

            env = jinja2.Environment(
                loader=jinja2.FileSystemLoader(folders)
            )

            for k, v in global_vars.items():
                env.globals[k] = v

            return env

        self.__saved = False

        self.zip = ZipFile(container, 'w')
        self.jenv = create_jinja_env()

        self.content = []
        self.rels = []

        # Adding style
        if style is None:
            style = Path.get_src(self.STYLES_FOLDER + "default.xml")

        self.add_relation(Xml(RelType.STYLE, "styles.xml", style))

    def __del__(self):
        if not self.__saved:
            self.save()
        try:
            if not self.__saved:
                self.save()
        except AttributeError:
            pass

    def add_relation(self, relation: Relation) -> int:
        """
        Method for adding external files (relations) to doc file
        :param relation: relation object
        :return: relation id
        """
        relation.id = len(self.rels) + 1
        self.rels.append(relation)
        return relation.id

    def save(self) -> None:
        """ Method for saving document (and delete object) """
        context = {
            'rels': self.rels,
            'content': self.content,
        }

        # Adding static files
        for file in Path.Utils.walk(Path.get_src(self.EMPTY_DOC_FOLDER)):
            template = self.jenv.get_template(file)
            self.zip.writestr(file, template.render(**context))

        # Adding relations
        for rel in self.rels:
            if rel.is_text:
                template = self.jenv.from_string(rel.content)
                self.zip.writestr('word/' + rel.target, template.render(rel.context))
            else:
                self.zip.write(rel.file, 'word/' + rel.target)

        self.zip.close()

        self.__saved = True
        del self

    def add_paragraph(self, text: str) -> None:
        """ Method for adding text paragraph to the document """
        lines = []
        for line in text.split('\n'):
            lines.append(f"<w:r><w:t>{line}</w:t></w:r>")
        lines = '\n'.join(lines)
        self.content.append(f"<w:p>{lines}</w:p>")

    def add_step(self, step_name: str, **context) -> None:
        """
        Method for rendering xml template (step)
        :param step_name: name of the step (without .xml)
        :param context: params to replace
        """
        filename, extension = Path.Utils.get_filename_and_extension(step_name)

        step = self.jenv.get_template(step_name + '.xml' if extension is None else '')
        self.content.append(step.render(**context))
