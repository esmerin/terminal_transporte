--gente que viajo a pereira
select cl.nombre,cl.apellido ,vb.id_bus,cl.cedula
from cliente cl inner join viajes_clientes_join vj
on  cl.id_cliente = vj.id_cliente
inner join viajes_en_bus vb
on vb.id_viaje = vj.id_viaje
where vb.destino = "pereira"
group by cl.cedula
limit 10;
-- los viajes que realizo cada bus a pereira
select count(*) as viajes , vb.id_bus
from cliente cl inner join viajes_clientes_join vj
on  cl.id_cliente = vj.id_cliente
inner join viajes_en_bus vb
on vb.id_viaje = vj.id_viaje
where vb.destino = "pereira"
group by vb.id_bus
order by viajes desc
limit 10;

-- los viajes que realizo un pasajero a diferentes regiones de colombia
-- el pasajero 8050 dado que habian muy pocos pasajeros y muchos viajes
-- es evidente que nadie viaja tanto en tan solo 2 meses
select vb.destino ,count(*) as Viajes_por_usuarios
from cliente cl inner join viajes_clientes_join vj
on  cl.id_cliente = vj.id_cliente
inner join viajes_en_bus vb
on vb.id_viaje = vj.id_viaje
where cl.id_cliente = 8050
group by vb.destino ;

-- los nombres de los usuarios que viajaron el en bus 7
-- entre el dia 31 de diciembre y el 2 de enero
select cl.nombre ,cl.cedula, vb.actual as terminal, vb.destino,vb.id_viaje, bus.placa
from cliente cl inner join viajes_clientes_join vj
on  cl.id_cliente = vj.id_cliente
inner join viajes_en_bus vb
on vb.id_viaje = vj.id_viaje
inner join bus on vb.id_bus = bus.id_bus
where vb.id_bus = 7 and vb.fecha_salida between "2019-12-31" and "2020-01-2";
-- promedio de edad de los pasajeros
select avg(cl.edad) as promedio_de_edad
from cliente cl inner join viajes_clientes_join vj
on  cl.id_cliente = vj.id_cliente
inner join viajes_en_bus vb
on vb.id_viaje = vj.id_viaje;
-- numero de menores de edad
select count(*) as menores_de_edad
from cliente cl inner join viajes_clientes_join vj
on  cl.id_cliente = vj.id_cliente
inner join viajes_en_bus vb
on vb.id_viaje = vj.id_viaje
where edad < 18;
-- porcentaje de menores de edad que viajaron a bogota,
--para esto hay que hacer una subconsulta

select count(*)/(select count(*)
                  from cliente cl inner join
                  viajes_clientes_join vj
                  on  cl.id_cliente = vj.id_cliente
                  inner join viajes_en_bus vb
                  on vb.id_viaje = vj.id_viaje
                  where vb.destino = "bogota" and cl.edad >18) * 100
    as porcentaje_menores_de_edad
from cliente cl inner join viajes_clientes_join vj
on  cl.id_cliente = vj.id_cliente
inner join viajes_en_bus vb
on vb.id_viaje = vj.id_viaje
where vb.destino = "bogota" and cl.edad < 18;

-- porcentaje de personas entre 20 y 30 a;os que viajaron a bogota
select count(*)/(select count(*)
                  from cliente cl inner join
                  viajes_clientes_join vj
                  on  cl.id_cliente = vj.id_cliente
                  inner join viajes_en_bus vb
                  on vb.id_viaje = vj.id_viaje
                  where vb.destino = "bogota") * 100
    as porcentaje_entre_20_30
from cliente cl inner join viajes_clientes_join vj
on  cl.id_cliente = vj.id_cliente
inner join viajes_en_bus vb
on vb.id_viaje = vj.id_viaje
where vb.destino = "bogota" and cl.edad < 30 and cl.edad >20;
