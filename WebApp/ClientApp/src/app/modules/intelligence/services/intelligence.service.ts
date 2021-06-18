import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { IImage } from '../interfaces/IImage';

@Injectable({
  providedIn: 'root',
})
export class IntelligenceService {
  private baseurl = environment.apiUrl + 'intelligence/';

  private getProcessedImagesUrl = this.baseurl + 'get';
  private uploadVideoUrl = this.baseurl + 'post';
 
  constructor(private http: HttpClient) {}

  public getProcessedImages(): Observable<IImage[]> {
    return this.http.get<IImage[]>(this.getProcessedImagesUrl);
  }

  public uploadVideo(model): Observable<any> {
    return this.http.post<any>(this.uploadVideoUrl, model, {
      // headers: this.generalService.getHttpHeaders(),
    });
  }
  
  // public acceptBookingStatus(id): Observable<any> {
  //   const httpParams = new HttpParams().set('id', id);
  //   // + '?id=' + id

  //   return this.http.patch(
  //     this.acceptBookingStatusUrl,
  //     {},
  //     {
  //       //headers: this.generalService.getHttpHeaders(),
  //       params: httpParams,
  //     }
  //   );
  // }
  // public acceptBookingStatus(id): Observable<any> {
  //   const httpParams = new HttpParams().set('id', id);
  //   // + '?id=' + id

  //   return this.http.patch(
  //     this.acceptBookingStatusUrl,
  //     {},
  //     {
  //       //headers: this.generalService.getHttpHeaders(),
  //       params: httpParams,
  //     }
  //   );
  // }
}
