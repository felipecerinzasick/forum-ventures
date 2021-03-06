import factory
import factory.django

from machina.core.db.models import get_model
from machina.test.factories.auth import UserFactory
from machina.test.factories.conversation import TopicFactory
from machina.test.factories.forum import ForumFactory


ForumReadTrack = get_model('forum_tracking', 'ForumReadTrack')
TopicReadTrack = get_model('forum_tracking', 'TopicReadTrack')


class ForumReadTrackFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    forum = factory.SubFactory(ForumFactory)

    class Meta:
        model = ForumReadTrack


class TopicReadTrackFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    topic = factory.SubFactory(TopicFactory)

    class Meta:
        model = TopicReadTrack
