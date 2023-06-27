from django.test import TestCase, RequestFactory
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect


from todo_list.models import Tag, Task
from todo_list.views import complete_undo_task


class ModelsTests(TestCase):
    def test_tag_str(self):
        tag = Tag.objects.create(name="test")
        self.assertEquals(str(tag), "test")

    def test_task_str(self):
        tag = Tag.objects.create(name="test")
        task = Task.objects.create(content="test")
        task.tags.add(tag)
        task.save()
        self.assertEquals(str(task), "test")


class NumbersViewsTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        self.task1 = Task.objects.create(content="Task 1")
        self.task2 = Task.objects.create(content="Task 2", is_active=False)
        self.tag1 = Tag.objects.create(name="Tag 1")
        self.tag2 = Tag.objects.create(name="Tag 2")

    def test_number_of_tasks_and_tags(self):
        response = self.client.get(reverse("todo_list:task-list"))

        # Check the response status code
        self.assertEqual(response.status_code, 200)

        # Get the context from the response
        context = response.context

        # Check if the expected keys are present in the context
        self.assertIn("num_tasks", context)
        self.assertIn("num_tags", context)

        # Check the values of num_tasks and num_tags
        self.assertEqual(context["num_tasks"], 2)
        self.assertEqual(context["num_tags"], 2)


class CompleteUndoTaskViewsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.tag = Tag.objects.create(name="Test Tag")
        self.task = Task.objects.create(content="Test Task", is_active=True)
        self.task.tags.add(self.tag)

    def test_complete_task(self):
        # Create a request object with the desired parameters
        request = self.factory.post(reverse_lazy("todo_list:finish-task", args=[self.task.pk]))

        # Call the view function
        response = complete_undo_task(request, pk=self.task.pk)

        # Check if the task was marked as complete
        self.task.refresh_from_db()
        self.assertFalse(self.task.is_active)

        # Check if the response is a redirect
        self.assertIsInstance(response, HttpResponseRedirect)

        # Check if the redirect URL is correct
        expected_url = reverse_lazy("todo_list:task-list")
        self.assertEqual(response.url, expected_url)

    def test_undo_task(self):
        # Mark the task as completed
        self.task.is_active = False
        self.task.save()

        # Create a request object with the desired parameters
        request = self.factory.post(reverse_lazy("todo_list:finish-task", args=[self.task.pk]))

        # Call the view function
        response = complete_undo_task(request, pk=self.task.pk)

        # Check if the task was marked as active (undo)
        self.task.refresh_from_db()
        self.assertTrue(self.task.is_active)

        # Check if the response is a redirect
        self.assertIsInstance(response, HttpResponseRedirect)

        # Check if the redirect URL is correct
        expected_url = reverse_lazy("todo_list:task-list")
        self.assertEqual(response.url, expected_url)
