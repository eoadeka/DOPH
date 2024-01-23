import markdown
from markdown_include.include import MarkdownInclude

# Markdown Extensions
source="index.md"
markdown_include = MarkdownInclude(
    configs={'inheritHeadingDepth':True}
)
html = markdown.markdown(source, extensions=[markdown_include])

md = markdown.Markdown(extensions=['pymdownx.snippets'])