import ujson as json
import urequests as requests
import utime as time
import select
import time_controller as time_cntrl
import gpio_controller as gpio_cntrl

gc.collect()


def make_request(url):
    global prices_str
    global datos_ordenados
    print("Cargando los datos...")
    response = requests.get(url)
    if response.status_code == 200:
        print("Datos cargados con éxito")
        data = response.json()
        datos = {}
        for hora in data.values():
            datos[hora["hour"]] = hora["price"]
        datos_ordenados = sorted(datos.items())
        prices = [precio for hora, precio in datos_ordenados]
        prices_str = list(map(str, prices))
    else:
        print("Error, no se pudieron cargar los datos")


def array_mas_baratos(valor):
    elementos = prices_str
    elementos_ordenados = sorted([float(p) for p in elementos])
    elementos_baratos = elementos_ordenados[:int(valor)]
    elementos_baratos_str = [str(p) for p in elementos_baratos]
    return elementos_baratos_str


def obtener_horas_mas_baratas(array, valor):
    datos_ordenados = sorted(array, key=lambda x: x[1])
    mas_baratos = datos_ordenados[:valor]
    horas_mas_baratas = [hora for hora, _ in mas_baratos]
    return horas_mas_baratas


def response_funct(conn):
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.close()


def web_page():
    html = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>ESP32 Luz</title>
    <style>

      .titulo {
        text-align: center;
      }
      .cabecera {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-evenly;
        align-items: center;
      }

      .container {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-evenly;
        align-items: flex-start;
        gap: 30px;
        margin-top: 80px;
        text-align: center;
      }

      .container-automatico {
        display: flex;
        flex-wrap: nowrap;
        flex-direction: row;
        gap: 20px;
      }

      .display {
        font-size: 50px;
        border: 1px solid black;
        border-radius: 10%;
        padding: 0 1rem 0 1rem;
      }

      .botones-auto {
        display: flex;
        flex-direction: column;
        flex-wrap: nowrap;
        gap: 3px;
      }

      .botones-auto button {
        width: 30px;
        height: 30px;
        font-size: 18px;
        border: 1px solid black;
        border-radius: 10%;
        background-color: #96e289;
        cursor: pointer;
      }

      .square {
        background-color: aquamarine;
        height: 4em;
        width: 6.5em;
        border-radius: 10px;
        margin: auto;
        display: flex;
        justify-content: center;
        align-items: center;
      }

      .square:hover {
        cursor: pointer;
      }

      .horas {
        display: grid;
        list-style-type: none;
        grid-template-columns: repeat(auto-fit, minmax(7em, 1fr));
        gap: 20px;
        border: 1px solid black;
        padding: 10px 10px 2px 10px;
        margin-top: 0px;
      }

      .dia {
        background-color: rgb(184, 184, 155);
        border-radius: 10px;
      }

      .noche {
        background-color: rgb(147, 143, 174);
        border-radius: 10px;
      }

      .titulo {
        text-align: center;
        font-size: 30px;
        font-style: bold;
        margin-top: none;
        padding: 10px;
      }
      .button {
        background-color: #e7bd3b;
        border: none;
        border-radius: 4px;
        color: white;
        padding: 16px 40px;
        text-decoration: none;
        font-size: 30px;
        cursor: pointer;
      }
      .button2 {
        background-color: #4286f4;
      }
      .button3 {
        background-color: #f44141;
      }

      .inline {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(10em, 1fr));
        gap: 2px;
        padding: 10px 10px 10px 10px;
      }

      .intervaloHoras {
        text-align: center;
        margin: 5px 0px 0px 0px;
        font-weight: bold;
        font-size: larger;
      }

      .precio {
        font-size: 25px;
        font-weight: bold;
      }

      .color-selected {
        background-color: #96e289;
        border: 3px solid black;
      }

      .border {
        border: 3px solid black;
      }
    </style>
  </head>"""
    html += f"""
  <body>
    <h1 class="titulo">ESP32 WebServer by tarik-dev</h1>
    <div class="cabecera">
      <h1>Hora de la útlima actualización: {hora_ultima_actualizacion}</h1>
      <h1>El precio medio de hoy es: {precio_medio}</h1>
    </div>

    <div class="dia">
      <div class="titulo">Mañana</div>
      <ul class="horas">
        <li>
          <div class="square ">
            <div class="precio">{prices_str[0]}</div>
          </div>
          <p class="intervaloHoras">00-01</p>
        </li>
        <li>
          <div class="square">
            <div class="precio">{prices_str[1]}</div>
          </div>
          <p class="intervaloHoras">01-02</p>
        </li>
        <li>
          <div class="square">
            <div class="precio">{prices_str[2]}</div>
          </div>
          <p class="intervaloHoras">02-03</p>
        </li>
        <li>
          <div class="square">
            <div class="precio">{prices_str[3]}</div>
          </div>
          <p class="intervaloHoras">03-04</p>
        </li>
        <li>
          <div class="square">
            <div class="precio">{prices_str[4]}</div>
          </div>
          <p class="intervaloHoras">04-05</p>
        </li>
        <li>
          <div class="square">
            <div class="precio">{prices_str[5]}</div>
          </div>
          <p class="intervaloHoras">05-06</p>
        </li>
        <li>
          <div class="square">
            <div class="precio">{prices_str[6]}</div>
          </div>
          <p class="intervaloHoras">06-07</p>
        </li>
        <li>
          <div class="square">
            <div class="precio">{prices_str[7]}</div>
          </div>
          <p class="intervaloHoras">07-08</p>
        </li>
        <li>
          <div class="square">
            <div class="precio">{prices_str[8]}</div>
          </div>
          <p class="intervaloHoras">08-09</p>
        </li>
        <li>
          <div class="square">
            <div class="precio">{prices_str[9]}</div>
          </div>
          <p class="intervaloHoras">09-10</p>
        </li>
        <li>
          <div class="square">
            <div class="precio">{prices_str[10]}</div>
          </div>
          <p class="intervaloHoras">10-11</p>
        </li>
        <li>
          <div class="square">
            <div class="precio">{prices_str[11]}</div>
          </div>
          <p class="intervaloHoras">11-12</p>
        </li>
      </ul>
    </div>
    <div class="noche">
      <div class="titulo">Tarde</div>
      <ul class="horas">
        <li>
          <div class="square">
            <div class="precio">{prices_str[12]}</div>
          </div>
          <p class="intervaloHoras">12-13</p>
        </li>
        <li>
          <div class="square">
            <div class="precio">{prices_str[13]}</div>
          </div>
          <p class="intervaloHoras">13-14</p>
        </li>
        <li>
          <div class="square">
            <div class="precio">{prices_str[14]}</div>
          </div>
          <p class="intervaloHoras">14-15</p>
        </li>
        <li>
          <div class="square">
            <div class="precio">{prices_str[15]}</div>
          </div>
          <p class="intervaloHoras">15-16</p>
        </li>
        <li>
          <div class="square">
            <div class="precio">{prices_str[16]}</div>
          </div>
          <p class="intervaloHoras">16-17</p>
        </li>
        <li>
          <div class="square">
            <div class="precio">{prices_str[17]}</div>
          </div>
          <p class="intervaloHoras">17-18</p>
        </li>
        <li>
          <div class="square">
            <div class="precio">{prices_str[18]}</div>
          </div>
          <p class="intervaloHoras">18-19</p>
        </li>
        <li>
          <div class="square">
            <div class="precio">{prices_str[19]}</div>
          </div>
          <p class="intervaloHoras">19-20</p>
        </li>
        <li>
          <div class="square">
            <div class="precio">{prices_str[20]}</div>
          </div>
          <p class="intervaloHoras">20-21</p>
        </li>
        <li>
          <div class="square">
            <div class="precio">{prices_str[21]}</div>
          </div>
          <p class="intervaloHoras">21-22</p>
        </li>
        <li>
          <div class="square">
            <div class="precio">{prices_str[22]}</div>
          </div>
          <p class="intervaloHoras">22-23</p>
        </li>
        <li>
          <div class="square">
            <div class="precio">{prices_str[23]}</div>
          </div>
          <p class="intervaloHoras">23-24</p>
        </li>
      </ul>
    </div>
    <div class="container">
      <div class="container-automatico">
        <button class="button" id="modo_automatico">Automático</button>
        <div class="display">0</div>
        <div class="botones-auto">
          <button class="button-increment"><b>+</b></button>
          <button class="button-decrement"><b>-</b></button>
        </div>
      </div>
      <!-- <button class="button button2" id="modo_semiautomatico">Semi-automático</button> -->
      <button class="button button3" id="modo_manual">Manual</button>
    </div> """
    html += """<script>
      document.addEventListener('DOMContentLoaded', function() {
        // Elementos del DOM
        const display = document.querySelector('.display');
        const incrementButton = document.querySelector('.button-increment');
        const decrementButton = document.querySelector('.button-decrement');
        const modoAutomaticoButton = document.getElementById("modo_automatico");
        const modoManualButton = document.getElementById("modo_manual");
        // const modoSemiAutomaticoButton = document.getElementById("modo_semiautomatico");

        let auto_on = false
        let semi_on = false
        let manual_on = false

        // Función para reiniciar los colores de cada square. Deberá ser implementada en cada botón para no crear confusión al cambiar de modos.
        function resetSelection() {
            // precios_manual = []
            const squares = document.querySelectorAll('.square');
            squares.forEach((square) => {
                square.classList.remove('color-selected');
            })
        }

        // Función seleccionar precios más baratos automático
        // También añade un borde al botón auto
        function precios_baratos_automatico(valor) {
          // reiniciamos el array referente a la selección de precio manual además de limpiar colores
          resetSelection();
          let elementos = document.querySelectorAll('.precio');
          let precios = []
          elementos.forEach((el) => {
            precios.push(parseFloat(el.innerText));
          });
          let precios_ordenados = precios.sort((a, b) => a - b);
          let precios_baratos = precios_ordenados.slice(0, valor);
          elementos.forEach((el) => {
            let precio = parseFloat(el.innerText);
            if(precios_baratos.includes(precio)) {
                el.parentNode.classList.add('color-selected');
            } else {
                el.parentNode.classList.remove('color-selected');
            }});
        modoAutomaticoButton.classList.add('border');
        // modoSemiAutomaticoButton.classList.remove('border');
        modoManualButton.classList.remove('border');
        }

        // Función semiautomática
        // Por el momento, clicar solo le añade borde y se lo quita a los otros dos
        function precios_semiautomaticos() {
            resetSelection();
            modoSemiAutomaticoButton.classList.add('border');
            modoAutomaticoButton.classList.remove('border');
            modoManualButton.classList.remove('border');
        }

        // Función manual
        // La dejaremos en un contexto global para mejorar la accesibilidad al usuario. Será la "por defecto". Cada vez que clickes en un número, pasaremos al modo manual.
        let precios_manual = [];
        function precios_manuales() {

            let lists = document.querySelectorAll('li');
            lists.forEach((list) => {
                list.addEventListener('click', () => {
                    if (auto_on) {
                    precios_manual = []
                    resetSelection()
                    console.log("aaaaaaaas")
                    manual_on = true
                    auto_on = false
                }
                    modoManualButton.classList.add('border');
                    modoAutomaticoButton.classList.remove('border');
                    // modoSemiAutomaticoButton.classList.remove('border');

                    const precio = list.querySelector('.intervaloHoras').innerText;
                    const index = precios_manual.indexOf(precio);

                    if(index > -1) {
                        precios_manual.splice(index, 1);
                        list.querySelector('li .square').classList.remove('color-selected');
                    } else {
                        precios_manual.push(precio);
                        list.querySelector('li .square').classList.add('color-selected');
                    }
                    console.log(precios_manual);
                    console.log(auto_on)
                    console.log(manual_on)
                });
            });
            console.log(precios_manual);
        }
        precios_manuales();

        // Funcionalidad +/- en display
        // Variable cantidad, que siempre es la misma que el display en pantalla
        let cantidad = 0;
        function incrementar() {
          cantidad++;
          if (cantidad > 24) {
            cantidad = 24;
          }
          display.textContent = cantidad;
        }
        function decrementar() {
          cantidad--;
          if (cantidad < 0) {
            cantidad = 0;
          }
          display.textContent = cantidad;
        }

        // Fetch functions
        function modo_automatico() {
          // ahora mismo solo mando el número de horas que selecciona el usuario. Podría mandar el array ya hecho
          auto_on = true
          semi_on = false
          manual_on = false
          fetch(`/modo_automatico?value=${cantidad}`, {method: 'GET'});
          precios_baratos_automatico(cantidad);
        }

        function modo_manual() {
            // Podemos hacer /modo_manual?value=${precios.join(',')}
          auto_on = false
          semi_on = false
          manual_on = true
          fetch(`/modo_manual?value=${precios_manual}`, {method: 'GET'});
        }

        function modo_semiautomatico() {
          fetch(`/modo_semiautomatico?value=0`, {method: 'GET'});
          precios_semiautomaticos();
        }

        // Listeners
        incrementButton.addEventListener('click', incrementar);
        decrementButton.addEventListener('click', decrementar);
        modoAutomaticoButton.addEventListener('click', modo_automatico);
        modoManualButton.addEventListener('click', modo_manual);
        // modoSemiAutomaticoButton.addEventListener('click', modo_semiautomatico);
      });
    </script>
  </body>
</html>
"""

    return html


URL_API_LUZ = "https://api.preciodelaluz.org/v1/prices/all?zone=PCB"
INTERVALO = 45000
ultima_actualizacion = time.ticks_ms()
hora_ultima_actualizacion = ""
precio_medio = 0
prices_str = ['0'] * 24
datos_ordenados = []

date_controller = time_cntrl.TimeController()
date_controller.cargar_hora()
gpio_controller = gpio_cntrl.GPIOController()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
print("Socket creado correctamente")
make_request(URL_API_LUZ)
ultima_actualizacion = time.ticks_ms()
date_controller.cargar_hora()

while True:
    gc.collect()
    ready_to_read, _, _ = select.select([s], [], [], 1)
    if s in ready_to_read:
        conn, addr = s.accept()
        print(f'Se ha conectado al socket {addr}')
        request = conn.recv(1024).decode()
        if request and '/modo_' in request:
            if '/modo_automatico' in request:
                print("automatico")
                valor = request.split('=')[1].split(' ')[0]
                if date_controller.hora_intervalo in obtener_horas_mas_baratas(
                        datos_ordenados, int(valor)):
                    print("exito, la hora coincide y se pueden enender los gpios")
                    gpio_controller.test_on()
                else:
                    print("la hora no coincide")
                    print(date_controller.hora_intervalo)
                    print(
                        obtener_horas_mas_baratas(
                            datos_ordenados,
                            int(valor)))
                    gpio_controller.test_off()
            elif '/modo_semiautomatico' in request:
                print("semi")
            elif '/modo_manual' in request:
                print("manual")
                valor = request.split('=')[1].split(' ')[0]
                array_valor = valor.split(',')
                if date_controller.hora_intervalo in array_valor:
                    print("exito, la hora coincide y se pueden encender los gpios")
                    gpio_controller.test_on()
                else:
                    print("la hora no coincide")
                    print(date_controller.hora_intervalo)
                    gpio_controller.test_off()
            response_funct(conn)
        else:
            print("pagina refrescada")
            gc.collect()
            response = web_page()
            conn.send('HTTP/1.1 200 OK\n')
            conn.send('Content-Type: text/html\n')
            conn.send('Connection: close\n\n')
            conn.sendall(response)
            conn.close()
    if time.ticks_diff(time.ticks_ms(), ultima_actualizacion) >= INTERVALO:
        gc.collect()
        make_request(URL_API_LUZ)
        ultima_actualizacion = time.ticks_ms()
        date_controller.cargar_hora()
        hora_ultima_actualizacion = date_controller.fecha_completa
        print(f"Hora última actualización: {hora_ultima_actualizacion}")
