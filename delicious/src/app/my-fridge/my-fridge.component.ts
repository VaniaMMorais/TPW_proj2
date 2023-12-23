import { Component, OnInit } from '@angular/core';
import { MyApiService } from '../my-api.service';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-my-fridge',
  templateUrl: './my-fridge.component.html',
  styleUrl: './my-fridge.component.css'
})
export class MyFridgeComponent implements OnInit{
  fridgeItems: any;
  ingredient: any;

  constructor(private authService: AuthService, private myApiService: MyApiService){}

  ngOnInit(): void {
    const currentUser = this.authService.getCurrentUser();
      this.myApiService.getFridgeData().subscribe(
        (data:any)=> {
          this.fridgeItems = data.filter((item: { user: any; }) => item.user === currentUser.user_id);
          this.fridgeItems.forEach((item: { ingredient: any; }) => {
            console.log(item.ingredient)
            this.getIngredient(item);
          });
          // this.loadIngredientDetails();
          console.log(this.fridgeItems);
        },
        (error: any) => {
          console.error('Error fetching data:', error);
        }
      )
  }

  onDelete(id: number): void{
    this.myApiService.deleteFridge(id).subscribe(
        () => {
          // Atualize a lista de itens após a exclusão
          location.reload();
        },
        (error) => {
          console.error('Erro ao excluir item:', error);
        }
      );
  }

  getIngredient(item: any): void {
    this.myApiService.getIngredientsById(item.ingredient).subscribe(
      (ingredientDetails: any) => {
        // Adicione os detalhes do ingrediente aos itens na geladeira
        item.ingredientDetails = ingredientDetails;
      },
      (error: any) => {
        console.error('Error fetching ingredient details:', error);
      }
    );
  }
}
