import json
import re
import sys
from pathlib import Path

NOVIDADES_URL = 'https://datago-dev.github.io/datago-public/static/novidades.html'
INSTALL_LINK_PATTERN = re.compile(r'https?://[^\s)]*installPackage\.apexp\?p0=(04t[A-Za-z0-9]{12,15})')
PLACEHOLDER_PATTERN = re.compile(r'04tX{3,}', re.IGNORECASE)
HEADING_PATTERN = re.compile(r'^##\s+(.+?)\s*$', re.MULTILINE)
MAX_NOTES = 6
RELEASE_FIELDS = ('id', 'tag_name', 'name', 'body', 'published_at', 'html_url')


class MissingPackageLink(Exception):
    pass


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


def is_public(release):
    return not release.get('draft') and not release.get('prerelease')


def build_releases_file(releases):
    public = [{field: release.get(field) for field in RELEASE_FIELDS} for release in releases if is_public(release)]
    return sorted(public, key=lambda release: release.get('published_at') or '', reverse=True)


def skip_reason(release, generated, existing):
    if release.get('draft'):
        return 'release é draft'
    if release.get('prerelease'):
        return 'release é pré-release'
    if existing and not is_newer_or_same(generated['releaseName'], existing.get('releaseName')):
        return f"release {generated['releaseName']} é mais antiga que a publicada {existing.get('releaseName')}"
    return None


def read_json(path):
    return json.loads(path.read_text(encoding='utf-8')) if path.exists() else None


def write_json(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def update_releases_file(releases_path, output_path):
    releases = json.loads(Path(releases_path).read_text(encoding='utf-8'))
    public = build_releases_file(releases)
    write_json(Path(output_path), public)
    print(f'{output_path} atualizado com {len(public)} versões')


def update_version_file(release_path, output_path):
    release = json.loads(Path(release_path).read_text(encoding='utf-8'))
    output = Path(output_path)
    generated = build_version_file(release)
    reason = skip_reason(release, generated, read_json(output))
    if reason:
        print(f'{output_path} mantido: {reason}')
        return
    if not generated['packageLink']:
        raise MissingPackageLink(f"release {generated['releaseName']} publicada sem link de pacote 04t válido; edite a release com o link e a Action roda de novo")
    write_json(output, generated)
    print(f"{output_path} atualizado para {generated['releaseName']}")


def main(release_path, releases_path, version_output, releases_output):
    update_releases_file(releases_path, releases_output)
    update_version_file(release_path, version_output)


if __name__ == '__main__':
    try:
        main(*sys.argv[1:5])
    except MissingPackageLink as error:
        print(f'ERRO: {error}')
        sys.exit(1)
