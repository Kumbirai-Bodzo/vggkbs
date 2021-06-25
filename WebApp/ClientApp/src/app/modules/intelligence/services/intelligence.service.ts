import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { IImage } from '../interfaces/IImage';

@Injectable({
  providedIn: 'root',
})
export class IntelligenceService {
  private baseurl = environment.apiUrl + 'intelligence/';
  private getProcessedImagesUrl = this.baseurl + 'predicted-list';
  private startPredictionProcessUrl = this.baseurl + 'start-prediction';
  private splitImagesFromVideoUrl = this.baseurl + 'split-images';
  private uploadVideoUrl = this.baseurl + 'post';

  constructor(private http: HttpClient) {}

  public getProcessedImages(): Observable<IImage[]> {
    return this.http.get<IImage[]>(this.getProcessedImagesUrl);
  }

  public startPredictionProcess(): Observable<any> {
    return this.http.get<any>(this.startPredictionProcessUrl);
  }
  public splitImagesFromVideo(): Observable<any> {
    return this.http.get<any>(this.splitImagesFromVideoUrl);
  }
  public uploadVideo(model): Observable<any> {
    return this.http.post<any>(this.uploadVideoUrl, model, {});
  }
}
