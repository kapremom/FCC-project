from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock

class HomePage(Page):
    body = StreamField(
        [
            ("raw_html", blocks.RawHTMLBlock(label="Raw HTML")),
            ("image", ImageChooserBlock(label="Image")),
            ("rich_text", blocks.RichTextBlock(label="Text")),
        ],
        blank=True,
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel("body", classname="Full"),
    ]
