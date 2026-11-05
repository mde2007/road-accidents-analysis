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

## Таблица 3. Collision (10 ключевых колонок)

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

`lsoa_of_collision_location` — England and Wales only (Scotland → NA).
