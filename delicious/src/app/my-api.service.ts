import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class MyApiService {
  private baseApiUrl = 'http://127.0.0.1:8000';
  constructor(private http: HttpClient) { }

  getIngredientsData(): Observable<any> {
    return this.http.get(this.baseApiUrl + '/ingredientes');
  }

  getCategoriesData(): Observable<any>{
    return this.http.get(this.baseApiUrl + '/categorias')
  }

  getRecipesData(): Observable<any>{
    return this.http.get(this.baseApiUrl + '/receitas')
  }

  getRecipesByIdData(id:any): Observable<any>{
    return this.http.get(this.baseApiUrl + '/receitas/'+id)
  }

  getCategoriesByIdData(id:number): Observable<any>{
    return this.http.get(this.baseApiUrl + '/categorias/' + id)
  }

  getRatingsData(): Observable<any>{
    return this.http.get(this.baseApiUrl + '/avaliacoes')
  }
}
