import { Component } from '@angular/core';
import { AuthService } from '../auth.service';
import { MyApiService } from '../my-api.service';

@Component({
  selector: 'app-favorites',
  templateUrl: './favorites.component.html',
  styleUrl: './favorites.component.css'
})
export class FavoritesComponent {
  favrecipes: any;
  recipes: any;
  user: any;
  favrecipe: any;

  constructor(private authService: AuthService, private myApiService: MyApiService){

  }

  ngOnInit(): void {
    const currentUser = this.authService.getCurrentUser();
  
    this.myApiService.getFavorites().subscribe(
      (data: any) => {
        this.favrecipes = data.filter((item: { user: any; }) => item.user === currentUser.user_id);
        console.log(this.favrecipes);
  
        // Mapear os IDs das receitas favoritas
        const favoriteRecipeIds = this.favrecipes.map((favRecipe: any) => favRecipe.receita);
  
        // Filtrar as receitas com base nos IDs das receitas favoritas
        this.myApiService.getRecipesData().subscribe(
          (recipesData: any) => {
            this.recipes = recipesData.filter((recipe: { id: any; }) => favoriteRecipeIds.includes(recipe.id));
            console.log(this.recipes);
          }
        );
      }
    );
  }

  removeFromFavorites(id: number) {
    const currentUser = this.authService.getCurrentUser();
  
    this.myApiService.getFavorites().subscribe(
      (data: any) => {
        this.favrecipes = data.filter((item: { user: any }) => item.user === currentUser.user_id);
        this.favrecipe = this.favrecipes.find((item: { receita: any }) => item.receita === id);
  
        if (this.favrecipe) {
          this.myApiService.deleteFavorite(this.favrecipe.id).subscribe(
            () => {
              // Atualizar a lista de favoritos após a remoção bem-sucedida
              this.favrecipes = this.favrecipes.filter((item: { receita: any }) => item.receita !== id);
              location.reload()
            },
            (error) => {
              console.error('Erro ao excluir favorito:', error);
            }
          );
        } else {
          console.error('Favorito não encontrado para remoção');
        }
      },
      (error) => {
        console.error('Erro ao obter favoritos:', error);
      }
    );
  }

    
}
