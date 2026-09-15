import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

GITHUB_DOCS_URL = 'https://github.com/DataGo-Dev/datago-public/blob/main/docs/'
TITLE_PATTERN = re.compile(r'^#[ \t]+(.+?)[ \t]*$', re.MULTILINE)
FENCED_CODE_PATTERN = re.compile(r'^```.*?^```', re.MULTILINE | re.DOTALL)
LINK_PATTERN = re.compile(r'\[([^\]]*)\]\([^)]*\)')
INLINE_MARKUP_PATTERN = re.compile(r'[*_`~]+')
SUMMARY_MAX_CHARS = 180
NON_PARAGRAPH_PREFIXES = ('#', '<', '!', '|', '```', '-', '*', '>')


def normalize_line_endings(text):
    return text.replace('\r\n', '\n').replace('\r', '\n')


def title_from(name, body):
    match = TITLE_PATTERN.search(FENCED_CODE_PATTERN.sub('', body))
    return match.group(1).strip() if match else humanize(name)


def humanize(name):
    return re.sub(r'[_-]+', ' ', name).strip().capitalize()


def body_without_title(body, title):
    lines = body.split('\n')
    for index, line in enumerate(lines):
        if TITLE_PATTERN.match(line) and line.lstrip('# ').strip() == title:
            return '\n'.join(lines[:index] + lines[index + 1:]).strip()
    return body.strip()


def is_paragraph_line(line):
    stripped = line.strip()
    return bool(stripped) and not stripped.startswith(NON_PARAGRAPH_PREFIXES) and not re.match(r'^\d+\.', stripped)


def first_paragraph(body):
    paragraph = []
    for line in body.split('\n'):
        if is_paragraph_line(line):
            paragraph.append(line.strip())
        elif paragraph:
            break
    return ' '.join(paragraph)


def plain_text(markdown):
    text = LINK_PATTERN.sub(r'\1', markdown)
    text = INLINE_MARKUP_PATTERN.sub('', text)
    return re.sub(r'\s+', ' ', text).strip()


def truncate(text, limit):
    if len(text) <= limit:
        return text
    cut = text[:limit].rsplit(' ', 1)[0]
    return cut.rstrip(' ,;:.') + '…'


def summary_from(body):
    return truncate(plain_text(first_paragraph(body)), SUMMARY_MAX_CHARS)


def last_commit_date(repo_root, path):
    result = subprocess.run(
        ['git', 'log', '-1', '--format=%cI', '--', str(path)],
        cwd=repo_root, capture_output=True, text=True,
    )
    committed = result.stdout.strip()
    if committed:
        return committed
    return datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).isoformat(timespec='seconds')


def build_doc(docs_dir, path):
    relative = path.relative_to(docs_dir).as_posix()
    body = normalize_line_endings(path.read_text(encoding='utf-8'))
    title = title_from(path.stem, body)
    content = body_without_title(body, title)
    return {
        'slug': relative[:-len(path.suffix)],
        'path': relative,
        'group': path.relative_to(docs_dir).parent.as_posix().replace('.', ''),
        'title': title,
        'summary': summary_from(content),
        'body': content,
        'updatedAt': last_commit_date(docs_dir.parent, path),
        'html_url': GITHUB_DOCS_URL + relative,
    }


def sort_key(doc):
    return (doc['group'] != '', doc['group'].lower(), doc['title'].lower())


def build_index(docs_dir):
    docs = [build_doc(docs_dir, path) for path in sorted(docs_dir.rglob('*.md'))]
    return sorted(docs, key=sort_key)


def write_json(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def main(docs_path, output_path):
    docs = build_index(Path(docs_path))
    write_json(Path(output_path), docs)
    print(f'{output_path} atualizado com {len(docs)} documentos')


if __name__ == '__main__':
    main(*sys.argv[1:3])
