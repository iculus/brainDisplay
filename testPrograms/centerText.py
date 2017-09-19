def render_multi_line(text, x, y, fsize):
        lines = text.splitlines()
        for i, l in enumerate(lines):
            screen.blit(sys_font.render(l, 0, hecolor), (x, y + fsize*i))