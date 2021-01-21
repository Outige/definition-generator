import imgkit
import pandas as pd 
import math

def generate_html(tag, source, title, text, img_src):
    html='''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=0.1">
    <link rel="stylesheet" href="tmp.css">
    <title>Document</title>
</head>
<body>
    <div class="container">
        <div id="inner-container">
            <h6>%s</h6>
            <h5>%s</h5>
            <div class="inner-inner">
                <h1 class="title">%s</h1>
                <img src="%s" alt="">
                <p>%s</p>
            </div>
        </div>
    </div>
</body>
</html>
    ''' % (tag, source, title, img_src, text)
    return html

def generate_css(border_colour, title_colour, text_colour, title_size, text_size, img_style):
    css = '''
body {
    padding: 0;
    margin: 0;
    background-color: white;
    display: block;
    width: 500px;
}
    '''

    css += '''
.container {
    border: 2px solid rgba(0, 0, 0, 1.0);
    width: 1036px;
    height: 1024px;
    text-align: center;
    background-color: white;
    margin: 0;
    padding: 0;
    display: inline-block;
}
    '''

    css += '''
#inner-container {
    border: 4px solid %s;
    background-color: white;
    width: 800px;
    height: 800px;
    margin: auto auto;
    position: relative;
    top: 10%c;
}
'''%(border_colour, '%')

    css += '''
.title {
    color: %s;
    font-size: %s;
}
    '''%(title_colour, title_size)

    css += '''
p {
    color: %s;
    font-size: %s;
    padding: 0 100px;
}
    '''%(text_colour, text_size)

    css += '''
h6 {
    /* display: block;
    float: right; */
    position: relative;
    top: -80px;
    font-size: 20px;
    text-align: right;
    color: #696b6e;
    /* position: absolute;
    margin-top: -100px;
    margin-left: -100px; */
}
    '''

    css += '''
.inner-inner {
    position: relative;
    top: -80px;
}
    '''

    css += '''
h5 {
    text-align: left;
    font-size: 19px;
    position: relative;
    top: 690px;
    color: #696b6e;
}
    '''

    css += '''
img {
    width: 250px;
    height: 250px;
    %s;
    
}
    ''' % (img_style)
    return css

def generate_definitions(input_csv):
    dataframe = pd.read_csv("in.csv")
    for i in range(len(dataframe)):

        img_src = ''
        if type(dataframe['image'][i]) in [str]:
            img_src = 'img/' + dataframe['image'][i]
        html = generate_html(dataframe['tag'][i], dataframe['source'][i], dataframe['title'][i], dataframe['text'][i], img_src)
        with open('static/tmp.html', 'w') as fp:
            fp.write(html)

        title_size = '80px'
        if len(dataframe['title'][i]) > 17:
            title_size = '50px'

        text_size = '50px'
        if len(dataframe['text'][i]) > 180:
            text_size = '35px'
        
        img_src = ''
        if type(dataframe['image'][i]) in [str]:
            img_src = dataframe['image'][i]
            img_style = '''    float: %s;
    margin-%s: 20px;
    margin-top: 20px;'''%(dataframe['image_pos'][i], dataframe['image_pos'][i])
        else:
            img_style = 'display: none'

        css = generate_css(dataframe['border_colour'][i], dataframe['title_colour'][i], dataframe['text_colour'][i], title_size, text_size, img_style)
        with open('static/tmp.css', 'w') as fp:
            fp.write(css)

        imgkit.from_file('static/tmp.html', 'out%d.jpg'%(i))


if __name__ == '__main__':
    generate_definitions('in.csv')
    import os
    os.remove("static/tmp.html")
    os.remove("static/tmp.css")