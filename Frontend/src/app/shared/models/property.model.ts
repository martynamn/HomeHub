export interface PropertyType {
  _id: string
  title: string
  price: number
  rooms: number
  type: string
  description: string
  userId: string
  creationDate: string
  adType: string
  telephoneNumber: string
  address: AddressType
  image: ImageType
}

export interface AddressType {
  country: string
  city: string
  floor: number
  postcode: string
  area: number
}

export interface ImageType {
  imageData: string
  filename: string
}