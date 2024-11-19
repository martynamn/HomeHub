/* This file contains app-wide general types */

/* Type used to match enum values with respecive string literal ane description */
export interface INameMapper {
  id: number;
  name: string;
  classType: string;
  description?: string;
  icon?: string;
}

/* Extension to skip enums that are not intent to be presented on viev (i.e. DEFAULT, ALL, e.c.t.) */
export interface IPrintableNameMapper extends INameMapper {
  isPrintable: boolean;
}
