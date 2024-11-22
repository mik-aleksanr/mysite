from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    preparation_steps = models.TextField()
    preparation_time = models.PositiveIntegerField()  # в минутах
    image = models.ImageField(upload_to='recipes/images/', null=True, blank=True)
    author = models.CharField(max_length=200)
    categories = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"
