import base64
from io import BytesIO
from flask import Flask
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)


@app.route("/")
def PieChart():
    fig = plt.Figure()
    ax = fig.add_axes([0,0,1,1])
    ax.axis('equal')

    # Setting properties
    names = ["POSITIVE", "NEGATIVE", "NEUTRAL"]
    colors_pie = ['#00DB29','#EC0400', '#F0F707']
    values = [1023, 4567, 903]
    ax.pie(values, labels = names, colors = colors_pie, autopct = "%1.2f%%"  )

    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
   
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"
    


if __name__ == "__main__":

    app.run(debug=True)