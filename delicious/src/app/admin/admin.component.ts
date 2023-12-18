import { Component, OnInit } from '@angular/core';
import { MyApiService } from '../my-api.service';
@Component({
  selector: 'app-admin',
  templateUrl: './admin.component.html',
  styleUrl: './admin.component.css'
})
export class AdminComponent implements OnInit {
  dataFromApi: any;

  constructor(private myApiService: MyApiService){}
  ngOnInit(): void {
    this.myApiService.getData().subscribe(
      (data: any) => {
        this.dataFromApi = data;
        console.log(data);
      },
      (error: any) => {
        console.error('Error fetching data:', error);
      }
    );
  }

}
