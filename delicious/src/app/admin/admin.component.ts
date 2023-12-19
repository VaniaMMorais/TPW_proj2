import { Component, OnInit } from '@angular/core';
import { MyApiService } from '../my-api.service';
@Component({
  selector: 'app-admin',
  templateUrl: './admin.component.html',
  styleUrl: './admin.component.css'
})
export class AdminComponent implements OnInit {
  ingredients: any;
  categories: any;

  constructor(private myApiService: MyApiService){}
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
  }

}
