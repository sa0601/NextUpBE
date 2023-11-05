from django.db import models

class Media(models.Model):
    # Define choices for media types
    MOVIE = 'Movie'
    SHOW = 'Show'
    GAME = 'Game'
    MEDIA_CHOICES = [
        (MOVIE, 'Movie'),
        (SHOW, 'Show'),
        (GAME, 'Game'),
    ]

    # Model fields
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    image_link = models.URLField(blank=True)  # Optional field for picture link
    priority = models.PositiveIntegerField(help_text="Enter a number to sort by priority.")
    tag = models.CharField(
        max_length=5,
        choices=MEDIA_CHOICES,
        default=MOVIE,
        help_text="Select a tag to categorize the media type."
    )

    def __str__(self):
        return f"{self.title} ({self.get_tag_display()})"

    class Meta:
        ordering = ['priority', 'title']  # Default ordering first by priority, then by title.

