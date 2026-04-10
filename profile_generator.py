def _get(preferences, key, default):
    value = preferences.get(key)
    return default if value is None else value


def _dots(count):
    if count <= 0:
        return ''
    return '.' * count


def _escape_xml(text):
    return (
        str(text)
        .replace('&', '&amp;')
        .replace('<', '&lt;')
        .replace('>', '&gt;')
        .replace('"', '&quot;')
        .replace("'", '&apos;')
    )


def _fmt_int(value):
    if value is None:
        return ''
    if isinstance(value, int):
        return f"{value:,}"
    return str(value)


def _leader_dots(label_text, value_text, target=28, min_dots=1):
    # approximate: target represents a fixed column width in characters
    label_len = len(str(label_text))
    value_len = len(str(value_text))
    dots = max(min_dots, target - label_len - value_len)
    return ' ' + ('.' * dots) + ' '


def load_ascii_art(filepath='ascii.txt'):
    """Load ASCII art from a text file, returning a list of lines."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = [line.rstrip('\n') for line in f.readlines()]
            # Filter out empty lines and return
            return [line for line in lines if line.strip()]
    except FileNotFoundError:
        print(f"Warning: {filepath} not found. Using default ASCII art.")
        return [
            '           g@M%@%%@N%Nw,,                   ',
            '        ,M*|`||*%gNM=]mM%g||%N,             ',
            "       p!``  '! |''` '''|||jhlj%w           ",
            "     ,@L `    ,,        ''!`|j%M]%M         ",
            "    ]j'` .,wp@pw,    `.     ''''|%Wg       ",
            '  /{||]@@@@@@@@@pp.             |||||      ',
        ]


def generate_profile_svg(username, preferences):
    """Generate SVGs that mimic the provided example structure/classes."""

    # Layout defaults match the example
    width = _get(preferences, 'width', '985px')
    height = _get(preferences, 'height', '400px')
    font_size = _get(preferences, 'font_size', '12px')
    font_family = _get(preferences, 'font_family', 'ConsolasFallback,Consolas,monospace')
    left_x = int(_get(preferences, 'left_x', 15))
    right_x = int(_get(preferences, 'right_x', 390))
    top_y = int(_get(preferences, 'top_y', 30))
    line_h = int(_get(preferences, 'line_height', 14))

    # Theme (dark) matches the example
    bg = _get(preferences, 'bg', '#161b22')
    fg = _get(preferences, 'fg', '#c9d1d9')
    key_color = _get(preferences, 'key_color', '#ffa657')
    value_color = _get(preferences, 'value_color', '#a5d6ff')
    add_color = _get(preferences, 'add_color', '#3fb950')
    del_color = _get(preferences, 'del_color', '#f85149')
    cc_color = _get(preferences, 'cc_color', '#616e7f')

    # Values (you will customize these)
    title = _escape_xml(_get(preferences, 'title', username))
    os_text = _escape_xml(_get(preferences, 'os', 'Windows 11'))
    uptime_text = _escape_xml(_get(preferences, 'uptime', '0 days'))
    host_text = _escape_xml(_get(preferences, 'host', 'My Host'))
    kernel_text = _escape_xml(_get(preferences, 'kernel', 'My Kernel'))
    ide_text = _escape_xml(_get(preferences, 'ide', 'VS Code'))

    langs_prog = _escape_xml(_get(preferences, 'languages_programming', _get(preferences, 'programming_langs', 'Python')))
    langs_comp = _escape_xml(_get(preferences, 'languages_computer', _get(preferences, 'computer_langs', 'HTML, CSS')))
    langs_real = _escape_xml(_get(preferences, 'languages_real', _get(preferences, 'real_langs', 'English')))

    hobby_soft = _escape_xml(_get(preferences, 'hobbies_software', _get(preferences, 'software_hobbies', '')))
    hobby_hard = _escape_xml(_get(preferences, 'hobbies_hardware', _get(preferences, 'hardware_hobbies', '')))

    email_personal = _escape_xml(_get(preferences, 'email_personal', _get(preferences, 'email', 'you@example.com')))
    email_secondary = _escape_xml(_get(preferences, 'email_secondary', ''))
    email_work = _escape_xml(_get(preferences, 'email_work', ''))
    linkedin = _escape_xml(_get(preferences, 'linkedin', ''))
    discord = _escape_xml(_get(preferences, 'discord', ''))

    repos = _escape_xml(_fmt_int(_get(preferences, 'repos', 0)))
    contrib = _escape_xml(_fmt_int(_get(preferences, 'contributed', _get(preferences, 'contrib_data', 0))))
    stars = _escape_xml(_fmt_int(_get(preferences, 'stars', 0)))
    commits = _escape_xml(_fmt_int(_get(preferences, 'commits', 0)))
    followers = _escape_xml(_fmt_int(_get(preferences, 'followers', 0)))
    loc_total = _escape_xml(_fmt_int(_get(preferences, 'lines_of_code', _get(preferences, 'loc_data', 0))))
    loc_add = _escape_xml(_fmt_int(_get(preferences, 'loc_add', 0)))
    loc_del = _escape_xml(_fmt_int(_get(preferences, 'loc_del', 0)))

    # ASCII art block - dynamically load from file
    ascii_file = _get(preferences, 'ascii_file', 'ascii.txt')
    ascii_lines = load_ascii_art(ascii_file)
    ascii_lines = [_escape_xml(line) for line in ascii_lines]

    ascii_tspans = []
    for idx, line in enumerate(ascii_lines):
        y = top_y + (idx * line_h)
        ascii_tspans.append(f'<tspan x="{left_x}" y="{y}">{line}</tspan>')

    # Dotted leaders (roughly like example; you can tune targets per row)
    os_dots = _escape_xml(_leader_dots('OS', os_text, target=34))
    uptime_dots = _escape_xml(_leader_dots('Uptime', uptime_text, target=34))
    host_dots = _escape_xml(_leader_dots('Host', host_text, target=34))
    kernel_dots = _escape_xml(_leader_dots('Kernel', kernel_text, target=34))
    ide_dots = _escape_xml(_leader_dots('IDE', ide_text, target=34))

    prog_dots = _escape_xml(_leader_dots('Languages.Programming', langs_prog, target=34))
    comp_dots = _escape_xml(_leader_dots('Languages.Computer', langs_comp, target=34))
    real_dots = _escape_xml(_leader_dots('Languages.Real', langs_real, target=34))

    hsoft_dots = _escape_xml(_leader_dots('Hobbies.Software', hobby_soft, target=34))
    hhard_dots = _escape_xml(_leader_dots('Hobbies.Hardware', hobby_hard, target=34))

    email1_dots = _escape_xml(_leader_dots('Email.Personal', email_personal, target=34))
    email2_dots = _escape_xml(_leader_dots('Email.Secondary', email_secondary, target=34))
    emailw_dots = _escape_xml(_leader_dots('Email.Work', email_work, target=34))
    linkedin_dots = _escape_xml(_leader_dots('LinkedIn', linkedin, target=34))
    discord_dots = _escape_xml(_leader_dots('Discord', discord, target=34))

    # GitHub Stats dotted leaders (these ids match today.py style so you can swap later)
    repo_dots = _escape_xml(_leader_dots('Repos', repos, target=10))
    star_dots = _escape_xml(_leader_dots('Stars', stars, target=18))
    commit_dots = _escape_xml(_leader_dots('Commits', commits, target=24))
    follower_dots = _escape_xml(_leader_dots('Followers', followers, target=14))
    loc_dots = _escape_xml(_leader_dots('Lines of Code on GitHub', loc_total, target=6))

    sep = _escape_xml(_get(preferences, 'separator', ' -———————————————————————————————————————————-—-'))
    sep2 = _escape_xml(_get(preferences, 'separator_contact', ' -——————————————————————————————————————————————-—-'))
    sep3 = _escape_xml(_get(preferences, 'separator_stats', ' -—————————————————————————————————————————-—-'))

    def tspan_line(y, content):
        return f'<tspan x="{right_x}" y="{y}">{content}</tspan>'

    y = top_y
    right_tspans = []
    right_tspans.append(tspan_line(y, f'{title}{sep}'))
    y += line_h

    right_tspans.append(
        f'<tspan x="{right_x}" y="{y}" class="cc">. </tspan><tspan class="key">OS</tspan>:'
        f'<tspan class="cc">{os_dots}</tspan><tspan class="value">{os_text}</tspan>'
    )
    y += line_h

    right_tspans.append(
        f'<tspan x="{right_x}" y="{y}" class="cc">. </tspan><tspan class="key">Uptime</tspan>:'
        f'<tspan class="cc" id="age_data_dots">{uptime_dots}</tspan><tspan class="value" id="age_data">{uptime_text}</tspan>'
    )
    y += line_h

    right_tspans.append(
        f'<tspan x="{right_x}" y="{y}" class="cc">. </tspan><tspan class="key">Host</tspan>:'
        f'<tspan class="cc">{host_dots}</tspan><tspan class="value">{host_text}</tspan>'
    )
    y += line_h

    right_tspans.append(
        f'<tspan x="{right_x}" y="{y}" class="cc">. </tspan><tspan class="key">Kernel</tspan>:'
        f'<tspan class="cc">{kernel_dots}</tspan><tspan class="value">{kernel_text}</tspan>'
    )
    y += line_h

    right_tspans.append(
        f'<tspan x="{right_x}" y="{y}" class="cc">. </tspan><tspan class="key">IDE</tspan>:'
        f'<tspan class="cc">{ide_dots}</tspan><tspan class="value">{ide_text}</tspan>'
    )
    y += int(line_h * 2)

    right_tspans.append(
        f'<tspan x="{right_x}" y="{y}" class="cc">. </tspan><tspan class="key">Languages</tspan>.<tspan class="key">Programming</tspan>:'
        f'<tspan class="cc">{prog_dots}</tspan><tspan class="value">{langs_prog}</tspan>'
    )
    y += line_h

    right_tspans.append(
        f'<tspan x="{right_x}" y="{y}" class="cc">. </tspan><tspan class="key">Languages</tspan>.<tspan class="key">Computer</tspan>:'
        f'<tspan class="cc">{comp_dots}</tspan><tspan class="value">{langs_comp}</tspan>'
    )
    y += line_h

    right_tspans.append(
        f'<tspan x="{right_x}" y="{y}" class="cc">. </tspan><tspan class="key">Languages</tspan>.<tspan class="key">Real</tspan>:'
        f'<tspan class="cc">{real_dots}</tspan><tspan class="value">{langs_real}</tspan>'
    )
    y += int(line_h * 2)

    right_tspans.append(
        f'<tspan x="{right_x}" y="{y}" class="cc">. </tspan><tspan class="key">Hobbies</tspan>.<tspan class="key">Software</tspan>:'
        f'<tspan class="cc">{hsoft_dots}</tspan><tspan class="value">{hobby_soft}</tspan>'
    )
    y += line_h

    right_tspans.append(
        f'<tspan x="{right_x}" y="{y}" class="cc">. </tspan><tspan class="key">Hobbies</tspan>.<tspan class="key">Hardware</tspan>:'
        f'<tspan class="cc">{hhard_dots}</tspan><tspan class="value">{hobby_hard}</tspan>'
    )
    y += int(line_h * 2)

    right_tspans.append(tspan_line(y, f'- Contact{sep2}'))
    y += line_h

    right_tspans.append(
        f'<tspan x="{right_x}" y="{y}" class="cc">. </tspan><tspan class="key">Email</tspan>.<tspan class="key">Personal</tspan>:'
        f'<tspan class="cc">{email1_dots}</tspan><tspan class="value">{email_personal}</tspan>'
    )
    y += line_h

    if email_secondary:
        right_tspans.append(
            f'<tspan x="{right_x}" y="{y}" class="cc">. </tspan><tspan class="key">Email</tspan>.<tspan class="key">Secondary</tspan>:'
            f'<tspan class="cc">{email2_dots}</tspan><tspan class="value">{email_secondary}</tspan>'
        )
        y += line_h

    if email_work:
        right_tspans.append(
            f'<tspan x="{right_x}" y="{y}" class="cc">. </tspan><tspan class="key">Email</tspan>.<tspan class="key">Work</tspan>:'
            f'<tspan class="cc">{emailw_dots}</tspan><tspan class="value">{email_work}</tspan>'
        )
        y += line_h

    if linkedin:
        right_tspans.append(
            f'<tspan x="{right_x}" y="{y}" class="cc">. </tspan><tspan class="key">LinkedIn</tspan>:'
            f'<tspan class="cc">{linkedin_dots}</tspan><tspan class="value">{linkedin}</tspan>'
        )
        y += line_h

    if discord:
        right_tspans.append(
            f'<tspan x="{right_x}" y="{y}" class="cc">. </tspan><tspan class="key">Discord</tspan>:'
            f'<tspan class="cc">{discord_dots}</tspan><tspan class="value">{discord}</tspan>'
        )
        y += line_h

    y += line_h
    right_tspans.append(tspan_line(y, f'- GitHub Stats{sep3}'))
    y += line_h

    # Two-column stats line (Repos/Contributed + Stars)
    right_tspans.append(
        f'<tspan x="{right_x}" y="{y}" class="cc">. </tspan><tspan class="key">Repos</tspan>:'
        f'<tspan class="cc" id="repo_data_dots">{repo_dots}</tspan><tspan class="value" id="repo_data">{repos}</tspan>'
        f' {{<tspan class="key">Contributed</tspan>: <tspan class="value" id="contrib_data">{contrib}</tspan>}}'
        f' | <tspan class="key">Stars</tspan>:<tspan class="cc" id="star_data_dots">{star_dots}</tspan><tspan class="value" id="star_data">{stars}</tspan>'
    )
    y += line_h

    # Commits + Followers
    right_tspans.append(
        f'<tspan x="{right_x}" y="{y}" class="cc">. </tspan><tspan class="key">Commits</tspan>:'
        f'<tspan class="cc" id="commit_data_dots">{commit_dots}</tspan><tspan class="value" id="commit_data">{commits}</tspan>'
        f' | <tspan class="key">Followers</tspan>:<tspan class="cc" id="follower_data_dots">{follower_dots}</tspan><tspan class="value" id="follower_data">{followers}</tspan>'
    )
    y += line_h

    # LoC line (total, add, del)
    right_tspans.append(
        f'<tspan x="{right_x}" y="{y}" class="cc">. </tspan><tspan class="key">Lines of Code on GitHub</tspan>:'
        f'<tspan class="cc" id="loc_data_dots">{loc_dots}</tspan><tspan class="value" id="loc_data">{loc_total}</tspan>'
        f' ( <tspan class="addColor" id="loc_add">{loc_add}</tspan><tspan class="addColor">++</tspan>, '
        f'<tspan class="delColor" id="loc_del">{loc_del}</tspan><tspan class="delColor">--</tspan> )'
    )

    style = f'''
<style>
@font-face {{
src: local('Consolas'), local('Consolas Bold');
font-family: 'ConsolasFallback';
font-display: swap;
-webkit-size-adjust: 109%;
size-adjust: 109%;
}}
.key {{fill: {key_color};}}
.value {{fill: {value_color};}}
.addColor {{fill: {add_color};}}
.delColor {{fill: {del_color};}}
.cc {{fill: {cc_color};}}
text, tspan {{white-space: pre;}}
</style>'''

    dark_svg = f"""<?xml version='1.0' encoding='UTF-8'?>
<svg xmlns=\"http://www.w3.org/2000/svg\" font-family=\"{font_family}\" width=\"{width}\" height=\"{height}\" font-size=\"{font_size}\">
{style}
<rect width=\"{width}\" height=\"{height}\" fill=\"{bg}\" rx=\"15\"/>
<text x=\"{left_x}\" y=\"{top_y}\" fill=\"{fg}\" class=\"ascii\">\n""" + "\n".join(ascii_tspans) + f"""\n</text>
<text x=\"{right_x}\" y=\"{top_y}\" fill=\"{fg}\">\n""" + "\n".join(right_tspans) + "\n</text>\n</svg>"

    # Light mode variant (simple palette swap)
    light = dark_svg
    light = light.replace(bg, _get(preferences, 'light_bg', '#ffffff'))
    light = light.replace(fg, _get(preferences, 'light_fg', '#24292f'))
    light = light.replace(key_color, _get(preferences, 'light_key_color', '#bc4c00'))
    light = light.replace(value_color, _get(preferences, 'light_value_color', '#0969da'))
    light = light.replace(cc_color, _get(preferences, 'light_cc_color', '#57606a'))
    light = light.replace(add_color, _get(preferences, 'light_add_color', '#1a7f37'))
    light = light.replace(del_color, _get(preferences, 'light_del_color', '#d1242f'))

    return dark_svg, light

def update_svg_files(username, preferences):
    """Update the SVG files with new data"""
    dark_svg, light_svg = generate_profile_svg(username, preferences)
    
    # Write to files
    with open('dark_mode.svg', 'w', encoding='utf-8') as f:
        f.write(dark_svg)
    
    with open('light_mode.svg', 'w', encoding='utf-8') as f:
        f.write(light_svg)
    
    print("✅ SVG files updated successfully!")

if __name__ == '__main__':
    # Your preferences - edit these!
    my_preferences = {
        'title': 'ThePixel@Pro',
        'os': 'Windows 11, Arch Linux',
        'uptime': '1 year, 2 months, 3 days',
        'host': 'Your Host',
        'kernel': 'Your Kernel',
        'ide': 'VS Code',
        'languages_programming': 'Python, JavaScript',
        'languages_computer': 'HTML, CSS',
        'languages_real': 'English, German',
        'hobbies_software': 'Web Development, KOReader Modifications',
        'hobbies_hardware': 'Modding Hardware',
        'email_personal': '',
        'email_secondary': '',
        'email_work': '',
        'linkedin': '',
        'discord': '',
        'repos': 0,
        'contributed': 0,
        'stars': 0,
        'commits': 0,
        'followers': 0,
        'loc_data': 0,
        'loc_add': 0,
        'loc_del': 0,
    }
    
    # Generate the SVG files
    update_svg_files('ThePixelPro366', my_preferences)
