# Process .docx, .xlsx, .pptx, .pdf files for office automation

from .util import Util
from .word import Word
from .excel import Excel
from .ppt import PPT
from .pdf import PDF
from .video import Video
import sys

__version__ = '0.2.6'
__author__ = "JoStudio"
__date__ = "2022/9/29"


# Open office files
def open_file(filename, template=None, **kwargs):
    """
    Open office files, such as .docx, .xlsx, .pptx, .pdf file

    :param filename:  file name
    :param template:  (optional) template file name.
        if template is not None, create filename by copy template file.
    :return: return object
    """
    ext = Util.file_ext(filename)
    if ext in ['.docx']:
        return Word(filename, template, **kwargs)
    elif ext in ['.xlsx']:
        return Excel(filename, template, **kwargs)
    elif ext in ['.pptx']:
        return PPT(filename, template, **kwargs)
    elif ext in ['.pdf']:
        return PDF(filename, template, **kwargs)
    else:
        raise ValueError('file extension % is not supported' % repr(ext))


def print_files(filename_list, **kwargs):
    """
    print files on default printer

    :param filename_list: list of file names
    :param kwargs:
    :return: None
    """
    for filename in filename_list:
        try:
            w = open_file(filename)
            w.print(**kwargs)
        except Exception as e:
            print("error print file %s, %s" % (filename, str(e)), file=sys.stderr)
