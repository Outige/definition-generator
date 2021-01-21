import imgkit
import pandas as pd 

def generate_html(title, text):
    html='''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=0.1">
    <link rel="stylesheet" href="test.css">
    <title>Document</title>
</head>
<body>
    <div class="container">
        <div id="inner-container">
            <h6>@conorosullyDS09d890uoh</h6>
            <div class="inner-inner">
                <h1 class="title">%s</h1>
                <p>%s</p>
            </div>
            <h5>Source: springboard.com/blog/data-science-terms/whgjgghkkg</h5>
        </div>
    </div>
</body>
</html>
    ''' % (title, text)
    return html

def generate_definitions(input_csv):
    dataframe = pd.read_csv("in.csv")
    # for x in dataframe:
    #     print(x)
    for i in range(len(dataframe)):
        # print(dataframe['title'][i])
        html = generate_html(dataframe['title'][i], dataframe['text'][i])
        with open('tmp.html', 'w') as fp:
            fp.write(html)
        imgkit.from_file('tmp.html', 'out%d.jpg'%(i))



if __name__ == '__main__':
    # imgkit.from_url('http://google.com', 'out.jpg')
    
    # imgkit.from_file('test.html', 'out.jpg')
    generate_definitions('in.csv')