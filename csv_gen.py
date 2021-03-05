from jinja2 import Template

if __name__ == '__main__':
    items = [
        {'inner_image': 'static/foo/b/1.jpg', 'outer_image': 'static/foo/b/1.jpg'},
        {'inner_image': 'static/foo/b/2.jpg', 'outer_image': 'static/foo/b/2.jpg'},
        {'inner_image': 'static/foo/b/3.jpg', 'outer_image': 'static/foo/b/3.jpg'},
        {'inner_image': 'static/foo/b/4.jpg', 'outer_image': 'static/foo/b/4.jpg'},
        {'inner_image': 'static/foo/b/5.jpg', 'outer_image': 'static/foo/b/5.jpg'},
        {'inner_image': 'static/foo/b/6.jpg', 'outer_image': 'static/foo/b/6.jpg'},
        {'inner_image': 'static/foo/b/7.jpg', 'outer_image': 'static/foo/b/7.jpg'},
        {'inner_image': 'static/foo/b/8.jpg', 'outer_image': 'static/foo/b/8.jpg'},
        {'inner_image': 'static/foo/b/9.jpg', 'outer_image': 'static/foo/b/9.jpg'},
        {'inner_image': 'static/foo/b/10.jpg', 'outer_image': 'static/foo/b/10.jpg'},
        {'inner_image': 'static/foo/b/11.jpg', 'outer_image': 'static/foo/b/11.jpg'},
        {'inner_image': 'static/foo/b/12.jpg', 'outer_image': 'static/foo/b/12.jpg'},
        {'inner_image': 'static/foo/b/13.jpg', 'outer_image': 'static/foo/b/13.jpg'},
    ]
    with open('template.csv', 'r') as fp:
        template_str = Template(fp.read())
        s = template_str.render(
            items=items
        )
        print(s)