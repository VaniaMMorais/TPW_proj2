import { Component, OnInit } from '@angular/core';
import { MyApiService } from '../my-api.service';
import { AuthService } from '../auth.service';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-my-fridge',
  templateUrl: './my-fridge.component.html',
  styleUrl: './my-fridge.component.css'
})
export class MyFridgeComponent implements OnInit{
  fridgeItems: any;
  ingredient: any;
  myForm: FormGroup;
  ingredientes: any[] | undefined;

  constructor(private fb: FormBuilder,private authService: AuthService, private myApiService: MyApiService){
    const currentUser = this.authService.getCurrentUser();
    this.myForm= this.fb.group({
      user:[currentUser.user_id],
      ingredient: [Validators.required],
      data:['2023-12-23'],
      checklist: [false]
    })

    this.fetchIngredientes();
  }

  ngOnInit(): void {
    const currentUser = this.authService.getCurrentUser();
      this.myApiService.getFridgeData().subscribe(
        (data:any)=> {
          this.fridgeItems = data.map((item: any, index: number) => ({ id: index + 1, ...item }));
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

  fetchIngredientes() {
    // Busque a lista de ingredientes da API
    this.myApiService.getIngredientsData().subscribe(
      (data) => {
        this.ingredientes = data;
      },
      (error) => {
        console.error('Erro ao buscar ingredientes:', error);
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

  onSubmit() {
    if (this.myForm.valid) {

      // Apenas envie se o formulário for válido
      this.myApiService.createFridge(this.myForm.value).subscribe(
        (response) => {
          console.log('Frigorífico criado com sucesso:', response);
          // Atualize localmente a lista ou faça outra ação, se necessário
          location.reload()
        },
        (error) => {
          console.error('Erro ao criar frigorífico:', error);
        }
      );
    }
  }

}
