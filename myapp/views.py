from django.shortcuts import render,redirect

from django.views.generic import View

from myapp.forms import MovieForm

from myapp.models import Movies

from django.contrib import messages



#view=>view for creating new movie
#method=>,get,post
#url=>localhost:8000/movie/add/

class MovieCreateView(View):

    def get(self,request,*args,**kwargs):

        form_instance=MovieForm()

        return render(request,'movie_add.html',{'form':form_instance})
    

    def post(self,request,*args,**kwargs):

        form_instance=MovieForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            Movies.objects.create(**data)

            messages.success(request,"movie has been added")

            return redirect("movie-list")
        
        else:

            messages.error(request,"failed to add movie")

            return render(request,'movie_add.html',{'form':form_instance})
        

#listing views
#method:GET
#url:localhost:8000/movies/all/


class MovieListView(View):

    def get(self,request,*args,**kwargs):
    
        qs=Movies.objects.all()

        return render(request,"movie_list.html",{"movies":qs})


#detail
#method:get
#url:localhost:8000/movie/<int:pk>

class MovieDetailView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Movies.objects.get(id=id)

        return render(request,'movie_detail.html',{'movie':qs})
    

#delete
#localhost:8000/movie/<int:pk>/remove/
#method:get

class MovieDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Movies.objects.get(id=id).delete()

        messages.success(request,"movie has been deleted")

        return redirect('movie-list')



#movie update view

class MovieUpdateview(View):
    
    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        movie_obj=Movies.objects.get(id=id) #select * from movie where id=2

        movie_dictionary={
            "title":movie_obj.title,
            "genre":movie_obj.genre,
            "language":movie_obj.language,
            "year":movie_obj.year,
            "run_time":movie_obj.run_time,
            "director":movie_obj.director
        }

        form_instance=MovieForm(initial=movie_dictionary)

        return render(request,'movie_edit.html',{'form':form_instance})
    

    def post(self,request,*args,**kwargs):

        form_instance=MovieForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            id=kwargs.get("pk")

            Movies.objects.filter(id=id).update(**data)

            messages.success(request,'movie has been updated')

            return redirect('movie-list')
        
        else:

            messages.error(request,'failed to update movie')
            
            return render(request,'movie_edit.html',{'form':form_instance})


    

    

        



