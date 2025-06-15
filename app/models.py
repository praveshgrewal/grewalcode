from django.db import models

class Testimonial(models.Model):
    ROLE_CHOICES = [
        ('Trainer', 'Trainer'),
        ('Student', 'Student'),
        ('Client', 'Client'),
    ]

    name = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Student')
    rating = models.PositiveSmallIntegerField(default=5)
    message = models.TextField()
    photo = models.ImageField(upload_to='testimonials/', default='default-user.png')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.role})"


class Blog(models.Model):
    CATEGORY_CHOICES = [
        ('Python', 'Python'),
        ('Cybersecurity', 'Cybersecurity'),
        ('AI/ML', 'AI/ML'),
        ('Cloud', 'Cloud'),
        ('Data Science', 'Data Science'),
        ('Data Analytics', 'Data Analytics'),
        ('DevOps', 'DevOps'),
        ('Machine Learning', 'Machine Learning'),
        ('Deep Learning', 'Deep Learning'),
        ('Java', 'Java'),
        ('Java Script', 'Java Script'),
        ('Web Development', 'Web Development'),
        
        
        
        
    ]
    
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    content = models.TextField()
    image = models.ImageField(upload_to='blogs/', default='default-blog.jpg')
    author = models.CharField(max_length=100, default='Admin')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title