import { Component, OnInit } from '@angular/core';
import { MyApiService } from '../my-api.service';

@Component({
  selector: 'app-admin',
  templateUrl: './admin.component.html',
  styleUrls: ['./admin.component.css']
})
export class AdminComponent implements OnInit {
  ingredients: any;
  categories: any;
  ingredientData: any = {
    nome: '',
    categoria: {
      id: null,
      nome: ''
    },
    icon: null,
    calorias: null
  };
  ingredientCategories: any[] = [];
  newCategory: any = {
    name:''
  };

  constructor(private myApiService: MyApiService) {}

  ngOnInit(): void {
    this.myApiService.getIngredientsData().subscribe(
      (data: any) => {
        this.ingredients = data;
        console.log(data);
      },
      (error: any) => {
        console.error('Error fetching data:', error);
      }
    );

    this.myApiService.getCategoriesData().subscribe(
      (data: any) => {
        this.categories = data;
        console.log(data);
      },
      (error: any) => {
        console.error('Error fetching data:', error);
      }
    );

    this.myApiService.getIngredientCategoryData().subscribe(
      (data: any) => {
        this.ingredientCategories = data;
        console.log(data);
      },
      (error: any) => {
        console.error('Error fetching data:', error);
      }
    );

    this.ingredientData.categoria = {
      id: null,
      nome: ''
    };
  }

  createIngredient() {
    // Verificar se a categoria foi selecionada
    if (this.ingredientData.categoria.id === null) {
      console.error('Por favor, selecione uma categoria.');
      return;
    }
    
    this.ingredientData.icon = 'null';

    console.log(this.ingredientData);

    this.myApiService.createIngredient(this.ingredientData).subscribe(
      (response) => {
        console.log('Ingrediente criado com sucesso:', response);
        // Faça algo após o sucesso, como limpar os campos do formulário
        this.resetForm();
        this.reloadIngredients();
        this.reloadPage();
      },
      (error) => {
        console.error('Erro ao criar ingrediente:', error);
        // Lide com erros, como exibir uma mensagem ao usuário
      }
    );
  }

  createCategory(){
    this.myApiService.createCategory(this.newCategory).subscribe(
      (response) => {
        console.log('Categoria criada com sucesso:', response);

        this.reloadPage();
      },
      (error) => {
        console.error('Erro ao criar categoria:', error);
        // Lide com erros, como exibir uma mensagem ao usuário
      }
    );
  }

  deleteIngredient(ingredientId: number): void {
    // Adicione a lógica de exclusão aqui, usando o ID do ingrediente
    this.myApiService.deleteIngredient(ingredientId).subscribe(
      (response)=> {
        console.log('Ingrediente eliminado com sucesso')
        this.reloadPage();
      }
    );
  }
  
  reloadPage() {
    // Recarregar a página
    location.reload();
  }

  reloadIngredients() {
    this.myApiService.getIngredientsData().subscribe(
      (data: any) => {
        this.ingredients = data;
        console.log('Lista de ingredientes recarregada:', data);
      },
      (error: any) => {
        console.error('Erro ao recarregar lista de ingredientes:', error);
      }
    );
  }
  

  resetForm() {
    // Limpar os campos do formulário
    this.ingredientData = {
      nome: '',
      categoria: {
        id: null,
        nome: ''
      },
      icon: null,
      calorias: null
    };
  }
}
