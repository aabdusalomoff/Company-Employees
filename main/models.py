from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)


    def __str__(self):
        return self.name 
    

class Book(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.PositiveIntegerField()
    genre = models.CharField(max_length=100,verbose_name='Kitob turi: ')
    published_year = models.DateField()
    author = models.ManyToManyField(Author,related_name='books')
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "book"
        verbose_name = 'Book'
        verbose_name_plural = 'Book'