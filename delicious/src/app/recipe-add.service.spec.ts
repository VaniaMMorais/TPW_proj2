import { TestBed } from '@angular/core/testing';

import { RecipeAddService } from './recipe-add.service';

describe('RecipeAddService', () => {
  let service: RecipeAddService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(RecipeAddService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
