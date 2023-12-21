import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, map } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class MyApiService {
  // private baseApiUrl = 'http://127.0.0.1:8000';
  private baseApiUrl = 'http://proj2tpw.pythonanywhere.com';
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
  getIngredientCategoryData(): Observable<any>{
    return this.http.get(this.baseApiUrl + '/categoria-ingredientes/')
  }

  createIngredient(ingredientData: any): Observable<any> {
    return this.http.post(this.baseApiUrl + '/criarIngrediente/', ingredientData).pipe(
      map((response: any) => response.id)
    );
  }

  createCategory(categoryData: any): Observable<any> {
    return this.http.post(this.baseApiUrl +'/categorias/', categoryData);
  }

  deleteIngredient(id: number): Observable<any>{
    return this.http.delete(this.baseApiUrl + '/ingredientes/' + id)
  }

  deleteCategory(id:number): Observable<any>{
    return this.http.delete(this.baseApiUrl + '/categorias/' + id)
  }

  login(header: any): Observable<any> {
    const url = this.baseApiUrl+'/api-auth/login/';
    return this.http.post(url, header);
  }

  getUser(): Observable<any> {
    return this.http.get(this.baseApiUrl + '/accounts/profile/');
  }

}
