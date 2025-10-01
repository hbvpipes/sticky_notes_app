# notes/tests.py
from django.test import TestCase
from django.urls import reverse
from .models import Note

class NoteModelTest(TestCase):
    def setUp(self):
        """Initialize test data for model testing"""
        Note.objects.create(
            title='Test Note', 
            content='This is a test note content.'
        )

    def test_note_creation_validation(self):
        """Verify successful creation and attribute assignment of Note instances"""
        note = Note.objects.get(id=1)
        self.assertEqual(note.title, 'Test Note')
        self.assertEqual(note.content, 'This is a test note content.')

    def test_string_representation(self):
        """Validate the string representation method returns expected format"""
        note = Note.objects.get(id=1)
        self.assertEqual(str(note), 'Test Note')

    def test_automatic_timestamp_generation(self):
        """Confirm automatic population of created_at and updated_at fields"""
        note = Note.objects.get(id=1)
        self.assertIsNotNone(note.created_at)
        self.assertIsNotNone(note.updated_at)

class NoteViewTest(TestCase):
    def setUp(self):
        """Prepare test data for view testing"""
        self.note = Note.objects.create(
            title='Test View Note', 
            content='This is a test for views.'
        )

    def test_note_listing_functionality(self):
        """Verify note list view returns correct response and template"""
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test View Note')
        self.assertTemplateUsed(response, 'notes/note_list.html')

    def test_note_creation_interface(self):
        """Validate note creation form accessibility"""
        response = self.client.get(reverse('note_create'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Create New Note')
        self.assertTemplateUsed(response, 'notes/note_form.html')

    def test_note_submission_processing(self):
        """Test successful note creation through form submission"""
        response = self.client.post(reverse('note_create'), {
            'title': 'New Test Note',
            'content': 'This is a new test note.'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Note.objects.count(), 2)

    def test_note_retrieval_for_editing(self):
        """Verify note editing interface loads correct data"""
        response = self.client.get(reverse('note_update', args=[self.note.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Edit Note')
        self.assertTemplateUsed(response, 'notes/note_form.html')

    def test_note_modification_processing(self):
        """Test successful note update functionality"""
        response = self.client.post(reverse('note_update', args=[self.note.id]), {
            'title': 'Updated Test Note',
            'content': 'This is an updated test note.'
        })
        self.assertEqual(response.status_code, 302)
        
        updated_note = Note.objects.get(id=self.note.id)
        self.assertEqual(updated_note.title, 'Updated Test Note')

    def test_note_removal_functionality(self):
        """Validate note deletion process"""
        response = self.client.get(reverse('note_delete', args=[self.note.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Note.objects.count(), 0)

    def test_empty_collection_handling(self):
        """Verify proper handling of empty note collections"""
        Note.objects.all().delete()
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No notes yet')
