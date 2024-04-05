from flask import Flask,render_template,url_for,flash,redirect
from forms import SearchForm,CreateForm
from db import DB
import pprint
app=Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
# posts=[
#     {
#         'author':'Challa Sai Charitha',
#         'title': 'Blog Post 1',
#         'content':'First post',
#         'date_posted':'May 22,2024'

#     },
#     {
#         'author':'Corey',
#         'title': 'Blog Post 2',
#         'content':'Second post',
#         'date_posted':'May 22,2024'

#     }
# ]
@app.route("/")
@app.route("/home")
def home():
    posts= DB().read_data()
    return render_template('home.html',posts=posts)
@app.route("/post")
def post():
    posts= DB().read_data()
    return render_template('post.html',posts=posts)


@app.route("/landing")
def landing():
    return render_template('landing.html')

@app.route("/about")
def about():
    posts= DB().read_data()
    return render_template('about.html',posts=posts)
@app.route("/search", methods=["POST"])
def search():
    form=SearchForm()
    tags= form.searched.data.split(" ")
    # print("TAGS",tags)
    get_posts= DB().find_data(tags)
    for i in get_posts:
        pprint.pprint(i)
    if(len(get_posts)==0):
        flash(f'No posts returned under this search term', 'error')
        return redirect(url_for("home"))

    return render_template("post.html",title='Search',posts=get_posts)

@app.route("/create", methods=['GET', 'POST'])
def create():
    form=CreateForm()
    if form.validate_on_submit():
        docu={"FirstName" :form.FirstName.data,
             "LastName" :form.LastName.data,
             "JobTitle" :form.JobTitle.data,
             "Overview" :form.Overview.data,
             "Level":form.Level.data,
             "Category":form.Category.data,
             "NumberofHours":form.NumberofHours.data,
             "MyStory":form.MyStory.data,
             "Email":form.Email.data,
             "linkedIn":form.LinkedIn.data,
             "content":form.content.data
             }
        docu["Category"]=str(docu["JobTitle"]).split(" ") + str(docu["Category"]).split(" ")
        obj=DB().add_data(docu)
        print(docu)
        
        
       

        flash(f'Data Stored for {form.FirstName.data}!', 'success')
        return redirect(url_for("home"))
  
    return render_template("create.html",title='Create',form=form)
if __name__ == '__main__':
    app.run(debug=True,port=5500)