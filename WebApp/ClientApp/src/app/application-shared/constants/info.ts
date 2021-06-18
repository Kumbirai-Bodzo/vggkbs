export class info {
  // failures
  public static email = 'reservations@adventurebookings.net';
  public static privacyEmail = null; // 'adventurebookings@gmail.com';
  public static supportEmail = 'support@adventurebookings.net';
  public static infoEmail = 'info@adventurebookings.net';
  public static reservationsEmail ='reservations@adventurebookings.net';
  public static domainName = 'adventurebookings.net';
  public static cell = null;
  public static facebook = 'https://facebook.com/adventurebookings.net';
  public static twitter = null; //'twitter';
  public static instagram = null; //'https://instagram.com';
  public static linkedin = null; // 'https://linkedin.com';

  public static intro = `
  Every moment of your adventure with us should feed your mind, heart, 
  soul – and your stomach. Whether it’s taking in the beauty Explorers’ 
  Village Restaurant or Shearwater Café, sitting under the canopies of 
  the Rainforest Café, or way up in the clouds at the Bridge Café; 
  international quality always meets local flavour.`;
}

export interface IInfo {
  intro: string;
  // email;
  privacyEmail: string;
  supportEmail: string;
  infoEmail:string;
  reservationsEmail: string;
  domainName: string;
  cell;
  facebook;
  twitter;
  instagram;
  linkedin;
}
