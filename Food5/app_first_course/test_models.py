import pytest
from .models import FirstCourse
from django.core.files.uploadedfile import SimpleUploadedFile

@pytest.mark.django_db
def test_create_first_course():
    image = SimpleUploadedFile("crema-de-calabaza-1.jpg", b"file_content", content_type="image/jpeg")
    fc = FirstCourse.objects.create(
        name="crema-de-calabaza",
        calories=150,
        vegan=True,
        gluten_free=True,
        purchase_price=2.50,
        retail_price=5.00,
        picture=image
    )
    assert fc.name == "crema-de-calabaza"
    assert fc.calories == 150
    assert fc.vegan is True
    assert fc.gluten_free is True
    assert fc.purchase_price == 2.50
    assert fc.retail_price == 5.00
    assert fc.picture is not None

""" from django.test import TestCase
from .models import FirstCourse
from django.core.files.uploadedfile import SimpleUploadedFile

class FirstCourseModelTest(TestCase):
    def test_create_first_course(self):
        # If you want to test image upload, use SimpleUploadedFile
        image = SimpleUploadedFile("crema-de-calabaza-1.jpg", b"file_content", content_type="image/jpeg")
        fc = FirstCourse.objects.create(
            name="crema-de-calabaza",
            calories=150,
            vegan=True,
            gluten_free=True,
            purchase_price=2.50,
            retail_price=5.00,
            picture=image  # or omit for no image
        )
        self.assertEqual(fc.name, "crema-de-calabaza")
        self.assertEqual(fc.calories, 150)
        self.assertTrue(fc.vegan)
        self.assertTrue(fc.gluten_free)
        self.assertEqual(fc.purchase_price, 2.50)
        self.assertEqual(fc.retail_price, 5.00)
        self.assertIsNotNone(fc.picture) """
