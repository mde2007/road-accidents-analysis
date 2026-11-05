# Словари данных: casualty / vehicle / collision (по guide 2025)

Единая терминология в «Пропуск (NA)?»: **NA** (`-1` — Data missing or out of range) / **unknown** (код `9` или `99` — self reported unknown, оставить категорией) / **не пропуск**.
`collision_year`, `*_reference`, `collision_index` — числа-идентификаторы, не категории.

## Таблица 1. Casualty (10 ключевых колонок)

| № | Колонка | Тип | Описание | Пропуск (NA)? |
|---|---|---|---|---|
| 1 | `collision_index` | int64 | Ключ столкновения | не пропуск |
| 2 | `collision_year` | int16 | Год (2021–2025) | не пропуск |
| 3 | `vehicle_reference` | int64 | Ключ ТС в столкновении | не пропуск |
| 4 | `casualty_reference` | int64 | Ключ пострадавшего | не пропуск |
| 5 | `casualty_class` | int8 | 1 driver/rider, 2 passenger, 3 pedestrian | не пропуск |
| 6 | `sex_of_casualty` | int8 | 1 male, 2 female, 9 unknown | unknown (9) / NA (-1) |
| 7 | `age_of_casualty` | int16 | Возраст | NA (-1) |
| 8 | `age_band_of_casualty` | int8 | 1–11 | NA (-1) |
| 9 | `casualty_severity` | int8 | 1 fatal, 2 serious, 3 slight (порядковая) | не пропуск |
| 10 | `casualty_type` | int16 | 0 pedestrian, 1 cyclist, 2–5 motorcycle, 8 taxi, 9 car, 10 minibus, 11 bus, 16 horse, 17 agri, 18 tram, 19 van, 20–21 goods, 22 mobility scooter, 23 — year-dependent (см. §1), 33 PPT (по conversion), 90 other, 97–99 unknown | unknown (99) / NA (-1) |

**Прочие колонки, не используются:** `casualty_imd_decile`, `lsoa_of_casualty`, `enhanced_casualty_severity`, `casualty_injury_based`, `casualty_adjusted_severity_serious`, `casualty_adjusted_severity_slight`, `casualty_distance_banding`, `escooter_flag`, `pedestrian_location`, `pedestrian_movement`, `car_passenger`, `bus_or_coach_passenger`, `pedestrian_road_maintenance_worker`.

## Таблица 2. Vehicle (10 ключевых колонок)

| № | Колонка | Тип | Описание | Пропуск (NA)? |
|---|---|---|---|---|
| 1 | `collision_index` | int64 | Ключ столкновения | не пропуск |
| 2 | `collision_year` | int16 | Год | не пропуск |
| 3 | `vehicle_reference` | int64 | Ключ ТС | не пропуск |
| 4 | `vehicle_type` | int16 | 1 pedal cycle, 2–5 motorcycle, 8 taxi, 9 car, 10 minibus, 11 bus, 16 horse, 17 agri, 18 tram, 19 van, 20–21 goods, 22 mobility scooter, **23 electric motorcycle**, 33 PPT, 90 other, 97–99 unknown | unknown (99) / NA (-1) |
| 5 | `age_of_driver` | int16 | Возраст водителя | NA (-1) |
| 6 | `sex_of_driver` | int8 | 1 male, 2 female, 3 not known | unknown (3) / NA (-1) |
| 7 | `vehicle_manoeuvre` | int16 | 1–20, 99 unknown | unknown (99) / NA (-1) |
| 8 | `engine_capacity_cc` | int32 | Объём двигателя | NA (-1) |
| 9 | `driver_imd_decile` | int8 | 1–10 (с 2016) | NA (-1) |
| 10 | `escooter_flag` | int8 | 1 yes, 0 no (поле с 2023) | NA (-1) для 2021–2022; 0/1 с 2023 |

## Таблица 3. Collision (19 ключевых колонок)

| № | Колонка | Тип | Описание | Пропуск (NA)? |
|---|---|---|---|---|
| 1 | `collision_index` | int64 | Ключ столкновения | не пропуск |
| 2 | `collision_year` | int16 | Год | не пропуск |
| 3 | `collision_severity` | int8 | 1 fatal, 2 serious, 3 slight (порядковая) | не пропуск |
| 4 | `number_of_vehicles` | int16 | Число ТС | не пропуск |
| 5 | `number_of_casualties` | int16 | Число пострадавших | не пропуск |
| 6 | `date` | datetime | DD/MM/YYYY | не пропуск |
| 7 | `time` | time | HH:MM | NA (null) |
| 8 | `police_force` | int16 | 1–99; 91–98 discontinued 2019; 99 Police Scotland с 2019 | не пропуск |
| 9 | `road_type` | int8 | 1 roundabout, 2 one way, 3 dual, 6 single, 7 slip, 9 unknown, 12 one way/slip | unknown (9) / NA (-1) |
| 10 | `urban_or_rural_area` | int8 | 1 urban, 2 rural, 3 unallocated | NA (-1) |
| 11 | `weather_conditions` | int8 | 1 fine no high winds, 2 raining no high winds, 3 snowing no high winds, 4 fine + high winds, 5 raining + high winds, 6 snowing + high winds, 7 fog or mist, 8 other, 9 unknown | unknown (9) / NA (-1) |
| 12 | `light_conditions` | int8 | 1 daylight, 4 darkness — lights lit, 5 darkness — lights unlit, 6 darkness — no lighting, 7 darkness — lighting unknown | NA (-1) |
| 13 | `road_surface_conditions` | int8 | 1 dry, 2 wet or damp, 3 snow, 4 frost or ice, 5 flood over 3cm deep, 6 oil or diesel, 7 mud, 9 unknown (self reported) | unknown (9) / NA (-1) |
| 14 | `speed_limit` | int8 | 20, 30, 40, 50, 60, 70 — единственно валидные на публичных дорогах | unknown (99, self reported) / NA (-1) |
| 15 | `longitude` | float | Долгота | NA (null) |
| 16 | `latitude` | float | Широта | NA (null) |
| 17 | `location_easting_osgr` | int32 | Easting OSGR | NA (null) |
| 18 | `location_northing_osgr` | int32 | Northing OSGR | NA (null) |
| 19 | `local_authority_district` | int16 | Код района (1–941); `-1` — code deprecated | NA (-1) |

`lsoa_of_accident_location` — England and Wales only (Scotland → NA).

Примечания: `longitude`/`latitude` и `location_easting_osgr`/`location_northing_osgr` — взаимозаменяемые пары координат, не категории; `speed_limit = 99` — unknown (self reported), не порядковая категория, не усреднять как число без обработки 99; `local_authority_district` — не `local_authority_ons_district` (ONS-код), это разные колонки.
