import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { MatDialogRef } from '@angular/material/dialog';
import { MyApiService } from '../my-api.service';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-recipe-add',
  templateUrl: './recipe-add.component.html',
  styleUrl: './recipe-add.component.css'
})
export class RecipeAddComponent {
  myForm: FormGroup;
  ingredientes: any;
  categories: any;

  constructor(private authService: AuthService,private fb: FormBuilder, public dialogRef: MatDialogRef<RecipeAddComponent>, private myApiService: MyApiService) {
    const currentUser = this.authService.getCurrentUser();
    this.myForm = this.fb.group({
      user: [currentUser.username],
      category: [Validators.required],
      name:  [Validators.required],
      description:  [Validators.required],
      tempoPreparacao: [Validators.required],
      tempoCozinhar: [Validators.required],
      quantidadePessoas: [Validators.required],
      nivel: [Validators.required],
      imagem: undefined,
      ingredients: {igrediente_nome: [Validators.required], quantidade: [Validators.required]},
    })

    this.fetchIngredientes();
    this.fetchCategories();
   }

  closeDialog(): void {
      this.dialogRef.close();
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

  fetchCategories() {
    // Busque a lista de ingredientes da API
    this.myApiService.getCategoriesData().subscribe(
      (data) => {
        this.categories = data;
      },
      (error) => {
        console.error('Erro ao buscar ingredientes:', error);
      }
    );
  }

  submitForm(){
    if (this.myForm.valid) {
      const recipeData = this.myForm.value;

      // Chame a função de criação de receita da sua API
      this.myApiService.createRecipe(recipeData).subscribe(
        (response) => {
          console.log('Receita adicionada com sucesso:', response);

          // Feche o diálogo após o sucesso
          this.dialogRef.close();
        },
        (error) => {
          console.error('Erro ao adicionar receita:', error);
        }
      );
    } else {
      console.error('Formulário inválido. Preencha todos os campos obrigatórios.');
    }
  }
}
