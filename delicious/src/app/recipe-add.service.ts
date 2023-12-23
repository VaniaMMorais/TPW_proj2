import { Injectable } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { RecipeAddComponent } from './recipe-add/recipe-add.component';

@Injectable({
  providedIn: 'root'
})
export class RecipeAddService {

  constructor(private dialog: MatDialog) { }

    openAddRecipeModal(): void {
        this.dialog.open(RecipeAddComponent, {
            width: '600px', // Ajuste o tamanho conforme necessário
        });
    }
}
