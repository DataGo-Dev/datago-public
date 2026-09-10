import json
import re
import sys
from pathlib import Path

NOVIDADES_URL = 'https://datago-dev.github.io/datago-public/static/novidades.html'
INSTALL_LINK_PATTERN = re.compile(r'https?://[^\s)]*installPackage\.apexp\?p0=(04t[A-Za-z0-9]{12,15})')
PLACEHOLDER_PATTERN = re.compile(r'04tX{3,}', re.IGNORECASE)
HEADING_PATTERN = re.compile(r'^##\s+(.+?)\s*$', re.MULTILINE)
MAX_NOTES = 6


def version_from_tag(tag):
    return re.sub(r'^v\.?', '', tag or '', flags=re.IGNORECASE).strip()


def version_parts(version):
    return [int(part) for part in re.findall(r'\d+', version or '')]


def is_newer_or_same(candidate, current):
    return version_parts(candidate) >= version_parts(current)


def stable_from(version):
    parts = version_parts(version)
    return f'{parts[0]}.{parts[1]}' if len(parts) >= 2 else version


def install_link_from(body):
    match = INSTALL_LINK_PATTERN.search(body)
    if not match or PLACEHOLDER_PATTERN.search(match.group(1)):
        return None
    return match.group(0)


def notes_from(body):
    return HEADING_PATTERN.findall(body)[:MAX_NOTES]


def build_version_file(release):
    version = version_from_tag(release.get('tag_name'))
    body = release.get('body') or ''
    return {
        'stable': stable_from(version),
        'releaseName': version,
        'packageLink': install_link_from(body),
        'link': f'{NOVIDADES_URL}#{version}',
        'notes': notes_from(body),
        'publishedAt': release.get('published_at'),
    }


def skip_reason(release, generated, existing):
    if release.get('draft'):
        return 'release é draft'
    if release.get('prerelease'):
        return 'release é pré-release'
    if not generated['packageLink']:
        return 'release sem link de pacote 04t válido'
    if existing and not is_newer_or_same(generated['releaseName'], existing.get('releaseName')):
        return f"release {generated['releaseName']} é mais antiga que a publicada {existing.get('releaseName')}"
    return None


def read_json(path):
    return json.loads(path.read_text(encoding='utf-8')) if path.exists() else None


def main(release_path, output_path):
    release = json.loads(Path(release_path).read_text(encoding='utf-8'))
    output = Path(output_path)
    generated = build_version_file(release)
    reason = skip_reason(release, generated, read_json(output))
    if reason:
        print(f'nitzap-version.json mantido: {reason}')
        return
    output.write_text(json.dumps(generated, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f"nitzap-version.json atualizado para {generated['releaseName']}")


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
