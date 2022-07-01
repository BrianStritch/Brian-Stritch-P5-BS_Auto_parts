from django import forms
from .models import ForumCategory, ForumPost, ForumPostComment, ForumTopics




class CreateForumPostForm(forms.ModelForm):
    """
        Class based form to set the fields in
        the Create Post model form for creating a new forum post
    """
    class Meta:
        """
        Class to indicate which model to use and to
        set the fields in the create review model form
        """
        model = ForumPost
        fields = (
            'title',
            'content',
            'summary',
            'topic',
            )

class ForumPostCommentForm(forms.ModelForm):
    """
    Class based form to create new comments using the
    comments model
    """
    class Meta:
        """
        Class to indicate which model to use and to
        set the fields in the create comment model form
        """
        model = ForumPostComment
        fields = ('body',) 

class ForumCategoryForm(forms.ModelForm):
    """
    Class BAsed form to create a new forum category using the topics model
    """
    class Meta:
        """
        Class to indicate which model to use and to
        set the fields in the create forum category model form
        """
        model = ForumCategory
        fields = ('name', 'friendly_name',)


class ForumTopicsForm(forms.ModelForm):
    """
    Class BAsed form to create a new forum topic using the topics model
    """
    class Meta:
        """
        Class to indicate which model to use and to
        set the fields in the create forum topic model form
        """
        model = ForumTopics
        fields = ('name', 'friendly_name', 'forum_category', 'summary')