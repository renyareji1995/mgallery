from django.db import models

class GenreChoices(models.TextChoices):

    ACTION='Action','Action'
    FICTION='Fiction','Fiction',
    TRILLER='Thriller','Thriller'

# choices using a variable
# GENRE_CHOICES=[('Action','Action'),
#               ('Fiction','Fiction'),
#                ('Thriller','Thriller')]



class Movies(models.Model):

    title=models.CharField(max_length=200)

    genre=models.CharField(max_length=200,choices=GenreChoices.choices)
    # genre=models.CharField(max_length=200,choices=GENRE_CHOICES)

    language=models.CharField(max_length=200)

    year=models.CharField(max_length=200)

    run_time=models.PositiveIntegerField()

    director=models.CharField(max_length=200)








# class ClassChoices(models.IntegerChoices):
#     ONE=(1,1)
#     TWO=(2,2)
#     THREE=(3,3)
#     FOUR=(4,4)
#     FIVE=(5,5)
#     SIX=(6,6)
#     SEVEN=(7,7)
#     EIGHT=(8,8)
#     NINE=(9,9)
#     TEN=(10,10)


# class DivisionChoices(models.TextChoices):
#     A=('A','A')
#     B=('B','B')
#     C=('C','C')
#     D=('D','D')


# class Student(models.Model):

#     name=models.CharField(max_length=200)

#     classs=models.CharField(max_length=200,choices=ClassChoices.choices)

#     division=models.CharField(max_length=200,choices=DivisionChoices.choices)

#     contact_no=models.CharField(max_length=200)

#     about_me=models.TextField()

#     image=models.ImageField()

#     url=models.URLField()




# class FuelClass(models.TextChoices):

#     PETROL=('petrol','petrol')

#     DIESEL=('diesel','diesel')

#     EV=('ev','ev')

# class Car(models.Model):

#     name=models.CharField(max_length=200)

#     model=models.CharField(max_length=200)

#     year=models.DateField(max_length=200)

#     seat_capacity=models.IntegerField(max_length=200)

#     fuel_type=models.CharField(max_length=200,choices=FuelClass.choices)

#     release_date=models.DateField()

#     performance=models.FloatField()

#     stock=models.BooleanField()

#     image=models.ImageField()


# class AboutUs(models.TextChoices):

#     NEWSPAPER=('Newspaper','Newspaper')
#     INTERNET=('Internet','Internet')
#     MAGAZINE=('Magazine','Magazine')
#     OTHERS=('Others','Others')

# class Recommendation(models.TextChoices):

#     YES=('Yes','Yes')
#     NO=('No','No')
#     MAYBE=('May be','May be')


# class Customer(models.Model):

#     first_name=models.CharField(max_length=200,null=False,blank=False)

#     last_name=models.CharField(max_length=200,null=False,blank=False)

#     address=models.CharField(max_length=200,null=False,blank=False)

#     street_address=models.CharFiled(max_length=200,null=False,blank=False)

#     address2=models.CharField(max_length=200,null=False,blank=False)

#     city=models.CharField(max_length=200)

#     state=models.CharField(max_length=200)

#     zip_code=models.CharField(max_length=200)

#     phone_number=models.CharField(max_lenth=200)

#     email=models.EmailField(max_length=200)

#     about_us=models.CharField(max_length=200,choices=AboutUs.choices)

#     feedback=models.TextField()

#     suggestions=models.TextField()

#     recommendation=models.CharField(max_length=200,choices=Recommendation.choices)


















