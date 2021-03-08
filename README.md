defgen is a package whose purpose is to turn structed inputs into stylish definitions.

# Stuctured inputs

defgen is able to handle 2 types of structed inputs: _CSV_ and _JSON_.

## CSV

| self description | title | text | source | source_colour | image | image_position | outer_image | outer_image_blur | inner_image | inner_image_blur | inner_gradient_direction | inner_gradient_start_colour | inner_gradient_end_colour | border_colour | border_width | border_radius | shadow_size | shadow_rgba | title_colour | text_colour | tag_colour | tag | font |
|------------------|-------|------|--------|---------------|-------|----------------|-------------|------------------|-------------|------------------|--------------------------|-----------------------------|---------------------------|---------------|--------------|---------------|-------------|-------------|--------------|-------------|------------|-----|------|
|                  |       |      |        |               |       |                |             |                  |             |                  |                          |                             |                           |               |              |               |             |             |              |             |            |     |      |

`self description`: (optional column) Helpful column to be able to summarize the very confusing and non-human settings required to generate the desired image.

`title`: The title text of the defintion.

`text`: The definition body.

`source`: The url crediting resources (images, explanations etc) used to create the definition.

`source_colour`: Hex value that sets the colour of the source.

`image`: Path to the supporting image of the definition. This path should be an exact relative path from the src code were the defgen functions are called, to where the image is located.

For example, if your directory looks like this.

```
.
├── main.py
├── static
│   └── images
│       ├── 3d-modeling.png
│       ├── artificial-intelligence.png
│       ├── cyborg.png
│       ├── explain.png
│       ├── sitebg.jpg
│       └── statistics.png
└── README.md
```

With your src code in _./main.py_ and you want to use _cyborg.png_ as your supporting image, then `image=static/images/cyborg.png`.

All _image paths_ will work the same.

`image_position`: The position of the text you want the supporing image to be. `left` for left of the text and `right` for right of the text.

`outer_image`: The path to the outer background image you want to use for your definition.

`outer_image_blur`: (non-negative float) Indicates how much of a blur you want to add to the outer image. 0 for no blur.

`inner_image`: The path to the inner background image you want to use for your definition.

`inner_image_blur`: (non-negative float) Indicates how much of a blur you want to add to the inner image. 0 for no blur.

`inner_gradient_direction`: The css property that describes the direction of the inner block's gradient. options=[to bottom left, to bottom right, to top left, to top right]. If this or any of the other gradient options are left blank, the gradient won't be applied.

`inner_gradient_start_colour`: Hex value of the starting colour of the inner gradient.

`inner_gradient_end_colour`: Hex value of the end colour of the outer gradient.

`border_colour`: Hex value of the colour of the inner boarder.

`border_width`: (non negative float) Pixel width of the inside border. 0 results in no border.

`border_radius`: (non negative float) Curvature of the inside border.

`shadow_size`: Pixel size of the inner border shadow.

`shadow_rgba`: A tuple of 4 values. The 1st the 3 values are Hex strings that represent Red, Green and blue respectivly. The last value represents the alpha value (opacity).

`title_colour`: Hex colour of the title.

`text_colour`: Hex colour of the text.

`tag_colour`: Hex colour of the tag.

`tag_font`: Font family of the text and title. Currently has no affect.

You can run csvs through `generate_definitions_from_csv`, either all in one or by selecting specific indexes to run.

### Annotated output

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

JSON represents an alternate format of an individual row in a csv. You can process a single definition's JSON with `generate_definition_from_json`.

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