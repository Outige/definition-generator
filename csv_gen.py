from jinja2 import Template

if __name__ == '__main__':
    items = [
        {'inner_image': 'static/foo/1.jpg', 'outer_image': 'static/foo/1.jpg'},
        {'inner_image': 'static/foo/2.jpg', 'outer_image': 'static/foo/2.jpg'},
        {'inner_image': 'static/foo/3.jpg', 'outer_image': 'static/foo/3.jpg'},
        {'inner_image': 'static/foo/4.jpg', 'outer_image': 'static/foo/4.jpg'},
        {'inner_image': 'static/foo/5.jpg', 'outer_image': 'static/foo/5.jpg'},
        {'inner_image': 'static/foo/6.jpg', 'outer_image': 'static/foo/6.jpg'},
        {'inner_image': 'static/foo/7.jpg', 'outer_image': 'static/foo/7.jpg'},
        {'inner_image': 'static/foo/8.jpg', 'outer_image': 'static/foo/8.jpg'},
        {'inner_image': 'static/foo/9.jpg', 'outer_image': 'static/foo/9.jpg'},
        {'inner_image': 'static/foo/10.jpg', 'outer_image': 'static/foo/10.jpg'},
        {'inner_image': 'static/foo/11.jpg', 'outer_image': 'static/foo/11.jpg'},
        {'inner_image': 'static/foo/12.jpg', 'outer_image': 'static/foo/12.jpg'},
        {'inner_image': 'static/foo/13.jpg', 'outer_image': 'static/foo/13.jpg'},
        {'inner_image': 'static/foo/14.jpg', 'outer_image': 'static/foo/14.jpg'},
    ]
    with open('template.csv', 'r') as fp:
        template_str = Template(fp.read())
        s = template_str.render(
            items=items
        )
        print(s)