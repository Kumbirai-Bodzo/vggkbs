/* tslint:disable:no-unused-variable */

import { TestBed, async, inject } from '@angular/core/testing';
import { IntelligenceService } from './intelligence.service';

describe('Service: Intelligence', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [IntelligenceService]
    });
  });

  it('should ...', inject([IntelligenceService], (service: IntelligenceService) => {
    expect(service).toBeTruthy();
  }));
});
