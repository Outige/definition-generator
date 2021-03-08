defgen is a package whose purpose is to turn structed inputs into stylish definitions.

# Stuctured inputs

defgen is able to handle 2 types of structed inputs: _CSV_ and _JSON_.

## CSV

| self description | title | text | source | source_colour | image | image_position | outer_image | outer_image_blur | inner_image | inner_image_blur | inner_gradient_direction | inner_gradient_start_colour | inner_gradient_end_colour | border_colour | border_width | border_radius | shadow_size | shadow_rgba | title_colour | text_colour | tag_colour | tag | font |
|------------------|-------|------|--------|---------------|-------|----------------|-------------|------------------|-------------|------------------|--------------------------|-----------------------------|---------------------------|---------------|--------------|---------------|-------------|-------------|--------------|-------------|------------|-----|------|
|                  |       |      |        |               |       |                |             |                  |             |                  |                          |                             |                           |               |              |               |             |             |              |             |            |     |      |

## JSON

```JSON
{
    "image_position": "left",
    "border_colour": "RED",
    "border_width": 4,
    "border_radius": 20,
    "title_colour": "#ffab40",
    "text_colour": "#696b6e",
    "outer_image": "static/foo/b/1.jpg",
    "outer_image_blur": 4,
    "inner_image": "static/foo/b/1.jpg",
    "inner_image_blur": 0,
    "inner_gradient_direction": null,
    "inner_gradient_start_colour": null,
    "inner_gradient_end_colour": null,
    "shadow_size": 20,
    "shadow_rgba": "0,0,0,0.4",
    "tag_colour": "#696b6e",
    "source_colour": "#535557",
    "text": "Some explanation",
    "image": "static/img/statistics.png",
    "title": "Random Forest",
    "source": "springboard.com/blog/data-science-terms/",
    "tag": "@conorosullyDS",
    "text_size": 38.0,
    "title_size": 80
}
```

# install
```
$ pip install defgen
```

# Example output
![out12](https://user-images.githubusercontent.com/41017214/109725016-313a4280-7bb9-11eb-91fb-8389f41eae44.jpg)
![out13](https://user-images.githubusercontent.com/41017214/109725093-4a42f380-7bb9-11eb-80c2-7a572e35ac53.jpg)

# Some pypi commands

pip install setuptools twine
python3 setup.py sdist
twine upload --repository-url https://upload.pypi.org/legacy/ --skip-existing dist/*

How to get using static files
Adding static files
How to use requirements.txt
Variable output dir
Rm prints