import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { MyApiService } from '../my-api.service';
import { faMagnifyingGlass, faStar as solidStar } from '@fortawesome/free-solid-svg-icons';
import { faStar as emptyStar } from '@fortawesome/free-regular-svg-icons';
import { Router } from '@angular/router';


@Component({
  selector: 'app-search-results',
  templateUrl: './search-results.component.html',
  styleUrl: './search-results.component.css'
})
export class SearchResultsComponent {
  recipes: any[] = [];
  search= faMagnifyingGlass;
  solidStar = solidStar;
  emptyStar = emptyStar;

  constructor(private route: ActivatedRoute, private myApiService: MyApiService, private router: Router) { }

  ngOnInit(): void {
    this.route.queryParams.subscribe(params => {
      const searchTerm = params['query'];
      if (searchTerm) {
        this.searchRecipes(searchTerm);
      }
    });
  }

  searchRecipes(searchTerm: string): void {
    // Chame o serviço ou método para buscar todas as receitas
    this.myApiService.getRecipesData().subscribe(
      (data: any) => {
        // Use a função filter para filtrar as receitas com base no nome
        this.recipes = data.filter((recipe: any) => {
          // Converta os nomes para minúsculas para uma comparação sem distinção entre maiúsculas e minúsculas
          const recipeNameLower = recipe.name.toLowerCase();
          const searchTermLower = searchTerm.toLowerCase();
  
          // Verifique se o nome da receita contém o termo de pesquisa
          return recipeNameLower.includes(searchTermLower);
        });
  
        console.log(this.recipes);
      },
      (error: any) => {
        console.error('Error fetching search results:', error);
      }
    );
  }
  navigateToRecipeDetails(recipeId: number): void {
    // Navegue para a rota '/recipeDetails' com o ID da receita como parâmetro
    this.router.navigate(['/recipeDetails', recipeId]);
  }
}
