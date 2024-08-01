from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase
from unittest import skip


class RecipeViewsTest(RecipeTestBase):

    def test_recipes_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    @skip('WIP')
    def test_recipe_home_template_shows_nothing_here_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            '<h1>Nothing here 😓</h1>',
            response.content.decode('utf-8')
        )

    def test_recipe_home_template_loads_recipes(self):
        # need a recipe for this test - fixture
        self.make_recipe(category_data={
            'name': 'Salgados'
        })
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')

        response_recipes = response.context['recipes']
        self.assertEqual(len(response_recipes), 1)
        self.assertEqual(response_recipes.first().title, 'Receita')

        self.assertIn('Receita', content)
        self.assertIn('10 Minutos', content)
        self.assertIn('5 porções', content)
        self.assertIn('Salgados', content)

    def test_recipe_home_template_dont_load_recipes_not_published(self):
        # need a recipe for this test - fixture
        self.make_recipe(is_published=False)
        response = self.client.get(reverse('recipes:home'))

        self.assertIn(
            '<h1>Nothing here 😓</h1>',
            response.content.decode('utf-8')
        )

    def test_recipes_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)

    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_category_template_loads_recipes(self):
        needed_title = 'Titulo da receita'
        # need a recipe for this test - fixture
        self.make_recipe(title=needed_title)
        response = self.client.get(reverse('recipes:category', args=(1,)))
        content = response.content.decode('utf-8')

        self.assertIn(needed_title, content)

    def test_recipe_category_template_dont_load_recipes_not_published(self):
        # need a recipe for this test - fixture
        recipe = self.make_recipe(is_published=False)
        response = self.client.get(
            reverse('recipes:category', args=(recipe.category.id,)))

        self.assertEqual(response.status_code, 404)

    def test_recipes_recipe_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)

    def test_recipe_recipe_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_recipe_template_loads_the_correct_recipe(self):
        needed_title = 'Titulo da receita detail'
        # need a recipe for this test - fixture
        self.make_recipe(title=needed_title)
        response = self.client.get(reverse('recipes:recipe', args=(1,)))
        content = response.content.decode('utf-8')

        self.assertIn(needed_title, content)

    def test_recipe_recipe_template_dont_load_recipe_not_published(self):
        # need a recipe for this test - fixture
        recipe = self.make_recipe(is_published=False)
        response = self.client.get(
            reverse('recipes:recipe', args=(recipe.id,)))

        self.assertEqual(response.status_code, 404)
